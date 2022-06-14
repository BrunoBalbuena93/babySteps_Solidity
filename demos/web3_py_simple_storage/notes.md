# Python 101 for Blockchain

### Setting up the environment
As many other applications, it is a best practice to create/initialize a virtual environment. In case the venv extension is not yet installed, should run that code too.
```
sudo apt-get install python3.X-venv
python3.X -m venv <venv>
```
Installing dependencies
1. **[py-solc-x](https://pypi.org/project/py-solc-x/)** Compiler for Solidity
2. **[web3](https://pypi.org/project/web3/)** Web3 Interface inspired in web3.js

Since we need to test on a "blockchain-like" environment, the course suggest to use [ganache](https://trufflesuite.com/ganache/), a test environment similar to the Javascript EVMs used in Remix.

### Hands on the example
For testing purposes, the file [simpleStorage.sol](/demos/web3_py_simple_storage/SimpleStorage.sol) was duplicated to serve here, this will be read into a variable and compiled using solcx's compile_standard module
```
from solcx import compile_standard

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
```
As it is shown, the version of Solidity is specified as the sources, output settings and configurations of the bytecode and abi, these data is regarding the contract to deploy, whereas HTTP/RCP is the blockchain where it will be deployed using the Web3 module

