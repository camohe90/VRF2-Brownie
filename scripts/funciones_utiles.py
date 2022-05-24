from brownie import accounts, config, network, web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development","ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork","mainnet-fork-dev"]


DECIMALS = 18
INITIAL_VALUE = web3.toWei(2000, "ether")
BASE_FEE = 100000000000000000  # The premium
GAS_PRICE_LINK = 1e9  # Some value calculated depending on the Layer 1 cost and Link
BLOCK_CONFIRMATIONS_FOR_VERIFICATION = 6


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])