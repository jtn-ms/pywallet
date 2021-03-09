pragma solidity ^0.4.20;

contract ECRecoverTest {
  function testRecovery() returns (address) {
    bytes32 h = 0x38d18acb67d25c8bb9942764b62f18e17054f66a817bd4295423adf9ed98873e;
    uint8 v = 27;
    bytes32 r = 0x723841761d213b60ac1cbf063207cbeba6c2725bcaf7c189e63f13d93fc1dc07;
    bytes32 s = 0x789d1dd423d25f0772d2748d60f7e4b81bb14d086eba8e8e8efb6dcff8a4ae02;

    return ecrecover(h, v, r, s);
  }
}