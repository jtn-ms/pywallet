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
    uint jackpot = 0;
    // constructor
    function Cleanify() public payable {
        creator = msg.sender;
        jackpot = jackpot.add(msg.value);
    }
    // Standard modifier on methods invokable only by contract creator.
    modifier onlyCreator {
        require (msg.sender == creator);
        _;
    }
    // increase exchange ether amount
    function donate() public payable{
        jackpot = jackpot.add(msg.value);
    }
    // withdraw amount to chosen addr.
    function withdraw(uint256 amount, bytes32 h, uint8 v, bytes32 r, bytes32 s) public onlyCreator returns (bool) {
        require(jackpot > amount, "withdraw amount can't be larger than jackpot");
        address toaddr = ecrecover(h, v, r, s);
        if (!toaddr.send(amount)) {
            return false;
        }
        jackpot = jackpot.sub(amount);
        return true;
    }
    // change creator
    function changeCreator(address _newCreator) external onlyCreator {
        require (_newCreator != creator,""onlyCreator methods called by non-creator");
        creator = _newCreator;
    }  
}