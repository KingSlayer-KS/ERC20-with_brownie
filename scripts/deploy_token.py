from brownie import My_token
from scripts.helpful_scripts import get_account
from web3 import Web3

inital_supply = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    mera_token = My_token.deploy(inital_supply, {"from": account})
    print(mera_token.name())
