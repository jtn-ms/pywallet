pragma solidity ^0.4.24;

contract Verifier {
    address public creator = address(0);
    address signer = address(0);
    // constructor
    function Verifier() public {
        creator = msg.sender;
    }
    // Standard modifier on methods invokable only by contract creator.
    modifier onlyCreator {
        require (msg.sender == creator);//, "OnlyCreator methods called by non-creator.");
        _;
    }
    function testRecovery(bytes32 h, uint8 v, bytes32 r, bytes32 s) returns (address) {
        // bytes memory prefix = "\x19Ethereum Signed Message:\n32";
        bytes memory prefix = abi.encodePacked(uint40(block.number);
        bytes32 prefixedHash = sha3(prefix, h);
        return ecrecover(prefixedHash, v, r, s);
    }
    //
    function verify(bytes32 rawhash, uint8 v, bytes32 r, bytes32 s) constant returns(bool) {
        return ecrecover(rawhash, v, r, s) == signer;
    }
    //
    function verifyEx(uint commitLastBlock, uint commit, uint8 v, bytes32 r, bytes32 s) constant returns(bool) {
        require (block.number <= commitLastBlock, "Commit has expired.");
        bytes32 signatureHash = keccak256(abi.encodePacked(uint40(commitLastBlock), commit));
        return ecrecover(signatureHash, v, r, s) == signer;
    }
    // change creator
    function changeCreator(address _newCreator) public onlyCreator {
        require (_newCreator != creator, "Cannot approve current creator.");
        creator = _newCreator;
    }  
    // change signer
    function changeCreator(address _newSigner) public onlyCreator {
        require (_newSigner != signer, "Cannot approve current creator.");
        signer = _newSigner;
    }
}