## Summary

The CTF solution uses Brownie and python tests

## Installation

To install Brownie development framework, follow the instructions [here](https://eth-brownie.readthedocs.io/en/stable/install.html)

## Exploits

#### ConfidentialHash

Variables on smart contract can be accessed independently from their modifiers using the “get_storage_at” RPC call

#### RoadClosed

Lack of access control enable malicious users to change contract owner

#### VipBank

Expected an underflow or a reentrancy but check-effects-interaction solution was being used. Only found a bad require condition that would lock funds of all users in the contract.

#### SafeNFT

Claim NFT is Vulnerable to reentrancy attack. Indeed, when executing an NFT safeTransfer function the contract will check if the sender implements onERC721Received function so that it is sure the sender knows how to handle NFT. onERC721Received can then be used to claim NFT until gas runs out. Check [smart contract](https://github.com/theexoticman/Quill-CTFs/blob/main/brownie/contracts/nft_hack.sol)

## Run exploits

to run all the exploits located in the [test file](https://github.com/theexoticman/Quill-CTFs/blob/main/brownie/tests/test_hack_script.py) run: `brownie test`
