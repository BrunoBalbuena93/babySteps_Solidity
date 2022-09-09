from .utils import get_account, get_contract, fund_link
from brownie import Lottery, config, network
from time import sleep

def deploy_lottery() -> None:
    '''
    '''
    account = get_account()
    Lottery.deploy(
        get_contract('eth_usd_price_feed').address,
        get_contract('vrf_coordinator').address, 
        get_contract('link_token').address, 
        config['networks'].get(network.show_active()).get('fee'),
        config['networks'].get(network.show_active()).get('keyhash'),
        {'from': account},
        publish_source = config['networks'].get(network.show_active()).get('verify', False)
        )
    print('Lottery deployed!')

def start_lottery() -> None:
    account = get_account()
    lottery = Lottery[-1]
    starting_tx = lottery.startLottery({'from': account})
    starting_tx.wait(1)
    print('Lottery has started')


def enter_lottery() -> None:
    '''
    '''
    account = get_account()
    lottery = Lottery[-1]
    value = lottery.getEntranceFee() + 100000000
    tx = lottery.enter({'from': account, 'value': value})
    tx.wait(1)
    print(f'Lottery entered {tx}')

def end_lottery() -> None:
    '''
    To end the lottery we would need to fund it with some LINK tokens
    '''
    account = get_account()
    lottery = Lottery[-1]
    tx = fund_link(lottery.address)
    print(type(tx))
    ending_tx = lottery.endLottery({'from': account})
    ending_tx.wait(1)
    sleep(60)
    print(f'Lottery finished, winner: {lottery.recentWinner()}')

def main():
    deploy_lottery()
    start_lottery()
    enter_lottery()
    end_lottery()