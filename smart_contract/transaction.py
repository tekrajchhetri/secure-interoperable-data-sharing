# -*- coding: utf-8 -*-
# @Time    : 19.11.22 13:18
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : https://tekrajchhetri.com/
# @File    : transaction.py
# @Software: PyCharm
import json
from web3 import Web3
import os
class Transaction:

    def __init__(self) -> None:
        # Test account address
        self.account_address="0xe3Fc9C5d3055ceb429F0F161E863151D19d4B2bF"
        # private key for test account
        self.private_key = "0xfadd56513d37277a3fe72518f0087fe26053df9f59dc95b97451f9a0a832fa57"
        self.chain_id = 1337
        self.URL = "http://138.232.18.143:8545"

    def get_contract_address(self):
        with open(f"{os.path.dirname(os.path.realpath(__file__))}/contract_address.json", 'r') as f:
            contract_details = json.load(f)
        return contract_details["contract_address"]

    def get_compiled_file_inforamtion(self):
        with open(f"{os.path.dirname(os.path.realpath(__file__))}/compiled_contract.json", 'r') as f:
            compiledsol_file = json.load(f)
        return compiledsol_file


    def decode_data(self, transactionHash):
        w3 = Web3(Web3.HTTPProvider(self.URL))
        compiledsol_file = self.get_compiled_file_inforamtion()
        abi = compiledsol_file['contracts']['contract.sol']['DataAccuracyVerifier']
        deployed_contract_instance = w3.eth.contract(address=self.get_contract_address(), abi=abi["abi"])
        decoded = deployed_contract_instance.decode_function_input(w3.eth.get_transaction(
            transaction_hash=transactionHash)['input'])
        print (f"DECODED DATA: {list(decoded)[1]['_token']} for transaction: {transactionHash}")
        return list(decoded)[1]['_token']

    def get_transaction_details(self, transactionHash):
        w3 = Web3(Web3.HTTPProvider(self.URL))
        return w3.eth.get_transaction(transaction_hash=transactionHash)

    def write_transactions(self, hash):
        import os
        if os.path.exists(f"{os.path.dirname(os.path.realpath(__file__))}/transactions.json"):
            with open(f"{os.path.dirname(os.path.realpath(__file__))}/transactions.json", "r") as file:
                hashdata = json.load(file)
                hashdata.update({f"transactions_hash_{len(hashdata) + 1}": hash})
            with open(f"{os.path.dirname(os.path.realpath(__file__))}/transactions.json", "w") as file:
                json.dump(hashdata, file)
        else:
            with open(f"{os.path.dirname(os.path.realpath(__file__))}/transactions.json", "w") as file:
                json.dump({f"transactions_hash_1": hash}, file)

        return True


    def create_transaction(self, data):
        compiledsol_file = self.get_compiled_file_inforamtion()
        abi = compiledsol_file['contracts']['contract.sol']['DataAccuracyVerifier']
        w3 = Web3(Web3.HTTPProvider(self.URL))
        #note the address change from initial contract creation
        deployed_contract_instance = w3.eth.contract(address=self.get_contract_address(), abi=abi["abi"])
        # read state:
        print(deployed_contract_instance.functions.retrieve().call())
        # update state:
        nonce = w3.eth.getTransactionCount(self.account_address)
        nounce = 0 if nonce == 0 else nonce + 2
        insert_new_data_to_contract = deployed_contract_instance.functions.setToken(
            str(data)
        ).buildTransaction({"chainId": self.chain_id,
                            "from": self.account_address,
                            "gasPrice": w3.eth.gas_price,
                            "nonce": nonce})
        # Sign the transaction
        sign_store_contact = w3.eth.account.sign_transaction(
            insert_new_data_to_contract, private_key=self.private_key
        )
        # Send the transaction
        send_store_contact = w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
        transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_contact)
        print(f"Transaction completed. Confirmation hash: {transaction_receipt['transactionHash'].hex()}. "
              f"Writing to hash to transactions.json")
        transactionHash=transaction_receipt['transactionHash'].hex()
        writejson = self.write_transactions(hash=transactionHash)
        if writejson:
            print("Writing successful")
        return transactionHash



if __name__ == '__main__':
    """Test script"""
    t = Transaction()
    transaction_hash = t.create_transaction(data="ASDFASDFa")
    print(t.decode_data(transaction_hash))
    print(t.get_transaction_details(transaction_hash))



