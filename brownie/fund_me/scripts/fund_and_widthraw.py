from brownie import FundMe
from .deploy import get_account

# Using different values because this is how the contract is developed
DECIMALS = 8
STARTING_PRICE = 200000000000
FUND_ME = FundMe[-1]

def fund():
    account = get_account()
    entrance_fee = FUND_ME.getEntranceFee()
    print(f'The current entry fee is {entrance_fee}')
    print('Funding')
    FUND_ME.fund({'from': account, 'value': entrance_fee})

def widthraw():
    print('widthrawing')
    FUND_ME.withdraw({'from': get_account()})

def main():
    fund()
    widthraw()