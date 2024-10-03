from web3 import Web3
import json
import os

# Connect to Base blockchain node
w3 = Web3(Web3.HTTPProvider('https://base-node-url'))  # Replace with actual Base node URL

# Check connection
if not w3.isConnected():
    raise ConnectionError("Failed to connect to the Base blockchain.")

# Load contract ABI and address
contract_address = '0xYourContractAddress'  # Replace with your contract address
with open(os.path.join(os.path.dirname(__file__), '..', 'contracts', 'MinesweeperABI.json')) as f:
    abi = json.load(f)

contract = w3.eth.contract(address=contract_address, abi=abi)

# Function to create NFT
def create_nft(player_address, private_key):
    nonce = w3.eth.get_transaction_count(player_address)
    txn = contract.functions.createNFT(player_address).buildTransaction({
        'chainId': 8453,  # Replace with Base's chain ID
        'gas': 2000000,
        'gasPrice': w3.toWei('5', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return w3.toHex(tx_hash)

# Additional blockchain interaction functions can be added here
