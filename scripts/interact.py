from src.blockchain import create_nft

def main():
    player_address = '0xPlayerAddress'  # Replace with player's address
    private_key = 'PlayerPrivateKey'    # Replace with player's private key
    tx_hash = create_nft(player_address, private_key)
    print(f"NFT creation transaction sent with hash: {tx_hash}")

if __name__ == "__main__":
    main()
