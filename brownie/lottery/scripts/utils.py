from brownie import accounts, network, config, Contract, interface
from brownie.network.transaction import TransactionReceipt
from brownie import MockV3Aggregator, VRFCoordinatorMock, LinkToken

DECIMALS = 8
INITIAL_VALUE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ('development', 'ganache-local')
FORKED_LOCAL_ENVIRONMENTS = ('mainnet-fork', 'mainnet-fork-dev')
CONTRACT_TO_MOCK = {'eth_usd_price_feed': MockV3Aggregator, 'vrf_coordinator': VRFCoordinatorMock, 'link_token': LinkToken}


def get_account(index: int=0, id: str=None) -> str:
    '''
    Making flexible the recovery of the account
    '''
    if index > 0:
        return accounts[index]
    elif id:
        return accounts.load(id)
    elif network.show_active() in (*LOCAL_BLOCKCHAIN_ENVIRONMENTS, *FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
    return accounts.add(config['wallets']['from_key'])


def deploy_mocks(decimals: int=DECIMALS, initial_value: int=INITIAL_VALUE):
    '''
    '''
    account = get_account()
    mock_price_feed = MockV3Aggregator.deploy(decimals, initial_value, {'from': account})
    print(f'Mock V3 Aggregator Deployed')
    link_token = LinkToken.deploy({'from': account})
    print(f'Mock Link Deployed')
    vrf_coordinator = VRFCoordinatorMock.deploy(link_token.address, {'from': account})
    print(f'Mock VRF Coordinator Deployed')

def fund_link(contract_address: str, account: str=None, link_token: str=None, amount: int=100000000000000000) -> TransactionReceipt:
    '''
    Fund link tokens
    '''
    account = account if account else get_account()
    link_token = link_token if link_token else get_contract('link_token')
    tx = link_token.transfer(contract_address, amount, {'from': account})
    tx.wait(1)
    print(f'Fund contract {tx}')
    return tx


def get_contract(contract_name: str) -> network.contract :
    '''
    Grab contract addresses from the brownie config if defined or create a mock and return it
    '''
    contract_type = CONTRACT_TO_MOCK.get(contract_name)
    # For development part (with mocking)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:
            deploy_mocks()
        contract = contract_type[-1]
    else:
        contract_address = config['networks'][network.show_active()][contract_name]
        contract = Contract.from_abi(contract_type._name, contract_address, contract_type.abi)
    return contract