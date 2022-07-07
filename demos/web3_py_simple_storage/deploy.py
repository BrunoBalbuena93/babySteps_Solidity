from json import dump
from solcx import compile_standard
from web3 import Web3
from os import getenv
from dotenv import load_dotenv

# For local ganache-cli
env = 'local'

# For rinkeby test net
# env = 'rinkeby'

# To use the ganache-cli
load_dotenv(dotenv_path=f'{env}.env')

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile Solidity

compiled_sol = compile_standard({
    'language': 'Solidity',
    'sources': {'SimpleStorage.sol': {'content': simple_storage_file}},
    'settings': {'outputSelection': {'*': {
        '*': ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']
    }}}
},
    solc_version='0.6.0')

with open('compiled_code.json', 'w') as file:
    dump(compiled_sol, file)

# Contract related data
# Get bytecode
bytecode = compiled_sol.get('contracts').get('SimpleStorage.sol').get(
    'SimpleStorage').get('evm').get('bytecode').get('object')
# Get ABI
abi = compiled_sol.get('contracts').get(
    'SimpleStorage.sol').get('SimpleStorage').get('abi')

# Blockchain related data
chain_address = Web3.HTTPProvider(getenv('RPC_SERVER'))
public_key_address = getenv('PUBLIC_ADDRESS')
private_key_address = getenv('PRIVATE_ADDRESS')
# Conecting to web3
web3 = Web3(chain_address)
simpleStorage = web3.eth.contract(abi=abi, bytecode=bytecode)
# Building a transaction
# 0. Getting last transaction
nonce = web3.eth.getTransactionCount(public_key_address)
# 1. Build the transaction
transaction = simpleStorage.constructor().buildTransaction(
    {'chainId': web3.eth.chain_id, 'from': public_key_address, 'nonce': nonce, 'maxFeePerGas': 2000000000, 'maxPriorityFeePerGas': 1000000000})
# 2. Sign transaction
signed_tx = web3.eth.account.sign_transaction(transaction, private_key_address)
# 3. Send transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
# 4. Transaction receipt
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# Working with the contract
# In order to do so, we will need the contract's address & abi
simple_storage = web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
# Calling reading functions: <contract>.functions.<function>.<type_of_call>
print(simple_storage.functions.retrieve().call())
# Calling write functions:
store_transaction = simple_storage.functions.store(15).buildTransaction(
    {'chainId': web3.eth.chain_id, 'from': public_key_address, 'nonce': nonce + 1, 'maxFeePerGas': 2000000000, 'maxPriorityFeePerGas': 1000000000}
    )
signed_store_txn = web3.eth.account.sign_transaction(store_transaction, private_key=private_key_address)
send_store_tx = web3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
send_store_receipt = web3.eth.wait_for_transaction_receipt(send_store_tx)

print(simple_storage.functions.retrieve().call())
