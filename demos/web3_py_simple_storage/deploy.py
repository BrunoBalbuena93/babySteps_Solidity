from json import dump
from solcx import compile_standard
from web3 import Web3
from os import getenv
from dotenv import load_dotenv

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile Solidity

compiled_sol = compile_standard({
    'language': 'Solidity',
    'sources': {'SimpleStorage.sol': {'content': simple_storage_file}},
    'settings': {'outputSelection':{'*': {
        '*': ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']
    }}}
    },
    solc_version='0.6.0')
    
with open('compiled_code.json', 'w') as file:
    dump(compiled_sol, file)

# Contract related data
# Get bytecode
bytecode = compiled_sol.get('contracts').get('SimpleStorage.sol').get('SimpleStorage').get('evm').get('bytecode').get('object')
# Get ABI
abi = compiled_sol.get('contracts').get('SimpleStorage.sol').get('SimpleStorage').get('abi')

# Blockchain related data
chain_address = Web3.HTTPProvider(getenv('RPC_SERVER'))
chain_id = getenv('NETWORK_ID')
public_key_address = getenv('PUBLIC_ADDRESS')
private_key_address = getenv('PRIVATE_ADDRESS')
# Conecting to web3
web3 = Web3(chain_address)
simpleStorage = web3.eth.contract(abi=abi, bytecode=bytecode)
# Building a transaction
# 0. Getting last transaction
nonce = web3.eth.getTransactionCount(public_key_address)
# 1. Build the transaction
transaction = simpleStorage.constructor().buildTransaction({'chainId': chain_id, 'from': public_key_address, 'nonce': nonce})
# 2. Sign transaction
signed_tx = web3.eth.account.sign_transaction(transaction, private_key_address)
