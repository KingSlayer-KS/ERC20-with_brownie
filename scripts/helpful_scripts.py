from brownie import accounts, config, network
from web3 import Web3

DECIMALS = 18
INITIALANSWER = 200000000000

FORKED_ENVS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_DEVELOPMENT_ENVS = ["development", "Ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_DEVELOPMENT_ENVS
        or network.show_active() in FORKED_ENVS
    ):
        return accounts[0]
    else:
        return accounts.add(config["Wallets"]["from_key"])