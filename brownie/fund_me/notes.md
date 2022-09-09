# Deploy Fund Me
## Networks

Brownie has several networks embedded already, if the command `brownie networks list` is run, brownie displays the networks in the different categories:
- Ethereum as the main, including the testnets like Rinkeby or Kovan
- Miscelaneous Net such as Polygon, Moonriver or xDai (all of these are in live chains)
- Development which are the networks brownie won't *remember* what it was deployed and they can be created and deleted on the flight

## Adding Mocks

Mocks are required when we want some interactions with third parties that are not deployed in our own local chain. In [fund me](/brownie/fund_me/contracts/FundMe.sol) it uses a chainlink contract to obtain the value of ETH in USD, but ganache does not know how to retrieve that since there's no contract deployed in local development chain which does that, for that reason, [deploy](/brownie/fund_me/scripts/deploy.py) creates a contract which returns a dummy predefined value and then it deploys the contract in hand (fund me)

## Adding Networks to Brownie

Sometimes we might wish that brownie does not forget about an existing local network, in such cases we register a local blockchain as a non development by using the following syntax:
```
brownie networks add <type> <name> host=<host> chainid=<chainid>
brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=1337
```

This way brownie will be calling to a network instead of running a client itself

# Forking

### Custom forking
To wrap things up we are going to create a fork of Ethereum mainnet and add it as a development net into brownie.

1. To start, we need to add a network as a development type, let's name it `mainnet-fork-dev`
2. It requires a command, a host and a place to take the fork from (here we are going to use a new application, not precisely Infura)
3. It needs some accounts to be setup and these accounts need a mnemonic phrase
4. Add where should it take the fork from (in here I'm using an alchemy endpoint)
```
brownie networks add development mainnet-fork-dev cmd=ganache-fork host=http://127.0.0.1 accounts=10 mnemonic=brownie port=8545 fork=$YOUR_OWN_ADDRESS
```