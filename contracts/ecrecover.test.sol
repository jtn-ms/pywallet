/*
PROVEN ALREADY
*/
pragma solidity ^0.4.24;

contract ECRecoverTest {
  function testRaw(bytes32 h, bytes32 r, bytes32 s) public returns (address) {
    return ecrecover(h, 27, r, s);
  }
  function testDice(uint commitLastBlock, uint commit, bytes32 r, bytes32 s) public returns (address) {
    bytes32 signatureHash = keccak256(abi.encodePacked(uint40(commitLastBlock), commit));
    return ecrecover(signatureHash, 27, r, s);
  }
}