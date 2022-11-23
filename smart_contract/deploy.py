# -*- coding: utf-8 -*-
# @Time    : 19.11.22 13:05
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : deploy.py
# @Software: PyCharm

from solcx import compile_standard
from web3 import Web3
import json


class DeployContract:
    def __init__(self) -> None:
        self.contract_file_name = "contract.sol"
        # account address of sender test account
        self.wallet = "0xE29a5B5a6193d3D3fe826F9D0D76feDeb712B872"
        # private key for test account
        self.private_key = (
            "0x1123e0c9c6df300c0cbdf61cbdca918716ca5e68fd306193aa61b345176d53d8"
        )
        self.chain_id = 1337
        self.URL = "http://138.232.18.143:8545"

    def read_contract(self, name):
        with open(name, "r") as file:
            contract_file = file.read()
        return contract_file

    def compile_contract(self, contract_file):
        """Compile the solidity smart contract
        :param contract_file: contract file
        :return: compiled solidity smart contract
        """
        compiled_contract = compile_standard(
            {
                "language": "Solidity",
                "sources": {"contract.sol": {"content": contract_file}},
                "settings": {
                    "outputSelection": {
                        "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                    }
                },
            },
            solc_version="0.8.12",
        )  # change the version based on your contract

        return compiled_contract

    def write_contract(self, compiled_contract):
        with open("compiled_contract.json", "w") as file:
            json.dump(compiled_contract, file)

    def deploy(self):
        read_contract = self.read_contract(self.contract_file_name)
        compiledsol_file = self.compile_contract(read_contract)
        self.write_contract(compiled_contract=compiledsol_file)
        abi = compiledsol_file["contracts"]["contract.sol"]["DataAccuracyVerifier"]
        bytecode = compiledsol_file["contracts"]["contract.sol"][
            "DataAccuracyVerifier"
        ]["evm"]["bytecode"]["object"]
        w3 = Web3(Web3.HTTPProvider(self.URL))
        contractsData = w3.eth.contract(abi=abi["abi"], bytecode=bytecode)
        nonce = w3.eth.getTransactionCount(self.wallet)
        transaction = contractsData.constructor().buildTransaction(
            {
                "gasPrice": w3.eth.gas_price,
                "chainId": self.chain_id,
                "from": self.wallet,
                "nonce": nonce,
            }
        )
        sign_transaction = w3.eth.account.sign_transaction(
            transaction, private_key=self.private_key
        )
        # Send the transaction
        transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
        # Wait for the transaction to be mined, and get the transaction receipt
        print(f"{transaction_hash}")
        transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
        print(
            f"Done! Contract deployed to {transaction_receipt.contractAddress}\n Writing contract details to file: contract_address.json"
        )
        with open("contract_address.json", "w") as file:
            json.dump({"contract_address": transaction_receipt.contractAddress}, file)


if __name__ == "__main__":
    d = DeployContract()
    d.deploy()
