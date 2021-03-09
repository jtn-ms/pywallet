/**
This contract was proved in htdf
*/
pragma solidity ^0.4.20;
// pragma experimental ABIEncoderV2;

library SafeMath {
  function mul(uint256 a, uint256 b) internal pure returns (uint256) {
	if (a == 0) {
		return 0;
	}
	uint256 c = a * b;
	assert(c / a == b);
	return c;
  }

  function div(uint256 a, uint256 b) internal pure returns (uint256) {
	uint256 c = a / b;
	return c;
  }

  function sub(uint256 a, uint256 b) internal pure returns (uint256) {
	assert(b <= a);
	return a - b;
  }

  function add(uint256 a, uint256 b) internal pure returns (uint256) {
	uint256 c = a + b;
	assert(c >= a);
	return c;
  }
}

contract Cleanify {
    using SafeMath for uint256;
    address public creator = address(0);
    uint accumulated = 0;
    // constructor
    function Cleanify() public payable {
        creator = msg.sender;
        accumulated = accumulated.add(msg.value);
    }
    // Standard modifier on methods invokable only by contract creator.
    modifier onlyCreator {
        require (msg.sender == creator);
        _;
    }
    // increase exchange ether amount
    function donate() public payable{
        accumulated = accumulated.add(msg.value);
    }
    // allocate amount to chosen addr.
    function allocate(uint256 amount, bytes32 h, uint8 v, bytes32 r, bytes32 s) public onlyCreator returns (bool) {
        require(accumulated > amount);
        // bytes memory prefix = "\x19Ethereum Signed Message:\n32";
        // bytes32 prefixedHash = keccak256(abi.encodePacked(uint40(100),h));
        address toaddr = ecrecover(h, v, r, s);
        if (!toaddr.send(amount)) {
            return false;
        }
        accumulated = accumulated.sub(amount);
        return true;
    }
    // allocate amount to chosen addr.
    function test() public onlyCreator returns (bool) {
        uint amount = 0x0000000000000000000000000000000000000000000000000000000000002710;
        bytes32 h = 0xee3a08ca29bf6f48a55b8a9b4563f6593a0c69f09f85daa07af646d62d5e774c;
        bytes32 r = 0x7146d41c235b013f135e53f9a11bfc3c2f8a969e61af72ab1ced71d4fdabded5;
        bytes32 s = 0x1c2d260a28f82e1e25367ff56799f31bfc403420d57b03668778334c7e5c3df8;
        uint8 v=27;
        require(accumulated > amount);
        address toaddr = ecrecover(h, v, r, s);
        if (!toaddr.send(amount)) {
            return false;
        }
        accumulated = accumulated.sub(amount);
        return true;
    }
    // change creator
    function changeCreator(address _newCreator) external onlyCreator {
        require (_newCreator != creator);
        creator = _newCreator;
    }  
}