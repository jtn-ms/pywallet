/**
not proven yet
*/
pragma solidity ^0.4.24;

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
    address public owner = address(0);
    uint accumulated = 0;
    // constructor
    constructor () public payable {
        owner = msg.sender;
        accumulated = accumulated.add(msg.value);
    }
    // Standard modifier on methods invokable only by contract owner.
    modifier onlyOwner {
        require (msg.sender == owner, "onlyOwner methods called by non-owner.");
        _;
    }
    // increase exchange ether amount
    function donate() public payable{
        accumulated = accumulated.add(msg.value);
    }
    // allocate amount to chosen addr.
    function allocate(address toaddr, uint256 amount) public external onlyOwner returns (bool) {
        require(accumulated > amount, "The request amount is unaffordable.");
        // transfer amount to chosen addr
        if (toaddr.send(amount)) { //sol-0.4.24
            return false;
        }
        accumulated = accumulated.sub(amount);
        return true;
    }
    // change owner
    function changeOwner(address _newOwner) external onlyOwner {
        owner = _newOwner;
    }  
}