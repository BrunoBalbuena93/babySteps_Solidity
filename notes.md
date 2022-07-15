# Solidity Course
[5:38:00](https://www.youtube.com/watch?v=M576WGiDBdQ&t=4s)


### Getting funds in rinkeby:
1. Go to https://faucet.rinkeby.io/ and click on the tweeter 3rd party
2. Create a tweet asking for the ETH (including your address)
3. Paste the tweet's url in the input field

### Some Infra

**Mnemonic:** Also known as seedphrase. This gives you access to all your accounts related to a wallet. (For example, *Metamask*)
**Private Key:**  
**Public Key:**

## Proof of Stake

- Works with collateral
- Validators are randomly chosen 

Pros:
1. Uses way less energy since it only works 1 node per block
2. The rest of the nodes just need to verify the block

### ETH proposal
Ethereum 2.0 is proposing to move from a *PoW* to a *PoS* blockchain, to do so it has a random number generator (provided from a Descentralized entity) to select which is gonna be the node to create the block. They are also including the concept of **sharding**, which is the solution of scalability in the blockchain, making -in a way- a blockchain of blockchain

### Developing Solidity

Enter to this link & start coding! Remember that Solidity needs to run on a Javascript VM (at least to do a few tests) or a Testnet

## Using Python
Since python is not the natural language to develop smart contracts, it uses some artifacts & tricks to develop and deploy. As an example, you can go to the [demo notes 101](/demos/web3_py_simple_storage/notes.md) to understand the workflow.


## Brownie
To install brownie, it is required to install `pipx`

The commands are:
```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```
It didn't work for me so I had to run it the first one, but with any of these should work:
```
pipx install eth-brownie
python3 -m pipx install eth-brownie
```

- **Build**: Tracks interfaces, deployments, chances and compiled code from smart contracts
- **Contracts**: Here is where it will try to find the contract files (*.sol), whenever you want to deploy it, it should be there
- **Interfaces**:
- **Reports**:
- **Scripts**: Automation and pipelines
- **Tests**: Create tests for QA purposes

If working with brownie and planning to use oracles, it is needed to do either a **fork** so it "thinks" it is communicating with other blockchain or **mock**

#### Mocking
With mocking, you are going to deploy a contract prior to the one you are working with, which will do the job as the external oracle. You could find the code for this in the chainlink [repo](https://github.com/smartcontractkit/chainlink-mix/tree/main/contracts/test)

## Verifying the smart contract
When we are deploying a smart contract, we can set it public and "ask" for the network to verify it. This example is shown in fund me [deploy script](/brownie/fund_me/scripts/deploy.py) 


## URLS
- Rinkeby ETH requester: https://faucet.rinkeby.io/
- ETH gas price: https://ethgasstation.info/
- ETH Units converter: https://eth-converter.com/
- Blockchain simulator: https://andersbrownworth.com/blockchain
- Solidity Editor: https://remix.ethereum.org/
- Infura: https://infura.io/
