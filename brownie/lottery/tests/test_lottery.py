from brownie import Lottery, accounts, config, network
from web3 import Web3

# Expected value: 0.0293756

def test_get_entrace_fee():
    '''
    '''
    account = accounts[0]
    lottery = Lottery.deploy(config['networks'][network.show_active()]['eth_usd_price_feed'], {'from': account})
    # assert lottery.getEntranceFee() > Web3.toWei(0.028, "ether")
    # assert lottery.getEntranceFee() < Web3.toWei(0.03, "ether")