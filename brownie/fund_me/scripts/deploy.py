from brownie import FundMe, network, accounts, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 18
STARTING_PRICE = 2000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ('development', 'ganache-local')
FORKED_LOCAL_ENVIRONMENTS = ('mainnet-fork', 'mainnet-fork-dev')

def get_account() -> str:
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])


def get_oracle_address() -> str:
    '''
    In order to keep the code cleaner, I'm separating the mocking/retrieval of the address in this function
    '''
    print(f'The current network is {network.show_active()}')
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
       return config['networks'][network.show_active()]
    if len(MockV3Aggregator) > 0:
        print('there is an instance of a prior mock, ')
        return MockV3Aggregator[-1].address
    print('Deploying mocks...')
    print(get_account())
    mock_aggregator = MockV3Aggregator.deploy(
        DECIMALS, Web3.toWei(STARTING_PRICE, 'ether'), {'from': get_account()})
    print('Mock deployed!')
    return mock_aggregator.address


def deploy_fund_me():
    account = get_account()
    # In case we are not looking into our own development environment
    price_feed_address = get_oracle_address()
    fund_me = FundMe.deploy(price_feed_address, {
                            'from': account}, 
                            publish_source=config['networks'][network.show_active()].get('verify')
                            )
    print(f'Contract deployed {fund_me.address}')
    return fund_me


def main():
    deploy_fund_me()
