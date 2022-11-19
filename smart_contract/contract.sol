pragma solidity ^0.8.12;

contract DataAccuracyVerifier {

    string token_to_verify;

    constructor(){
        token_to_verify="TEST123";
    }

    function setToken(string memory _token) public {
        token_to_verify = _token;
    }

    function retrieve() public view returns (string memory){
        return token_to_verify;
    }
}