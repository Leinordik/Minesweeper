from web3 import Web3
import json
import os

# Connect to Base blockchain node
w3 = Web3(Web3.HTTPProvider('https://base-node-url'))  # Replace with actual Base node URL

# Check connection
if not w3.isConnected():
    raise ConnectionError("Failed to connect to the Base blockchain.")

# Read compiled contract
contract_path = os.path.join(os.path.dirname(__file__), '..', 'contracts', 'Minesweeper.json')
with open(contract_path) as f:
    contract_json = json.load(f)
    contract_abi = contract_json['abi']
    contract_bytecode = contract_json['bytecode']

# Set up account
account = w3.eth.account.from_key('YOUR_PRIVATE_KEY')  # Replace with your private key
w3.eth.default_account = account.address

# Deploy contract
Minesweeper = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
tx_hash = Minesweeper.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Contract deployed at address: {tx_receipt.contractAddress}")
