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
    address public creator = address(0);
    uint accumulated = 0;
    // constructor
    function Cleanify() public payable {
        creator = msg.sender;
        accumulated = accumulated.add(msg.value);
    }
    // Standard modifier on methods invokable only by contract creator.
    modifier onlyCreator {
        require (msg.sender == creator);//, "OnlyCreator methods called by non-creator.");
        _;
    }
    // increase exchange ether amount
    function donate() public payable{
        accumulated = accumulated.add(msg.value);
    }
    // allocate amount to chosen addr.
    function allocate(address toaddr, uint256 amount) public external onlyCreator returns (bool) {
        require(accumulated > amount, "The request amount is unaffordable.");
        // transfer amount to chosen addr
        if (toaddr.send(amount)) { //sol-0.4.24
            return false;
        }
        accumulated = accumulated.sub(amount);
        return true;
    }
    // change creator
    function changeCreator(address _newCreator) public external onlyCreator {
        require (_newCreator != creator, "Cannot approve current creator.");
        creator = _newCreator;
    }  
}