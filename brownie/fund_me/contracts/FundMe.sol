// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract FundMe {
    using SafeMathChainlink for uint256;
    
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }
    
    function fund() public payable {
        uint256 minimumUSD = 50* 10 **18;
        require(getConversionRate(msg.value) >= minimumUSD, "You need more ETH!");
        addressToAmountFunded[msg.sender] += msg.value;    
        funders.push(msg.sender);
        }

    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }
    
    function withdraw() public onlyOwner payable {
        msg.sender.transfer(address(this).balance);
        for (uint256 funderIndex=0; funderIndex<funders.length; funderIndex++) {
            addressToAmountFunded[funders[funderIndex]] = 0;
        }
        funders = new address[](0);
    }
 
    function getVersion() public view returns (uint256) {
        // El argumento del contrato es la dirección del contrato que se puede encontrar en docs.chain.link/docs/ethereum-addresses/

        return priceFeed.version();
    }
    
    function getPrice() public view returns(uint256) {
        // Rinkeby
        (,int256 answer,,,) = priceFeed.latestRoundData();
        // Los 0's son porque la respuesta viene en WEI
        return uint256(answer * 10000000000);
    }
    
    function getConversionRate(uint256 ethAmount) public view returns (uint256) {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUSD = (ethPrice * ethAmount) / 10000000000;
        return ethAmountInUSD;
    }
}