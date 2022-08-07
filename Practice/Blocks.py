from datetime import datetime
from hashlib import sha256

class Block:
    def __init__(self, transactions, previous_hash, nonce = 0):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.nonce = nonce
        self.hash = self.generate_hash()

    def generate_hash(self):
        blocks_contents = str(self.transactions) + str(self.previous_hash) + str(self.timestamp) + str(self.nonce) 
        block_hash = sha256(blocks_contents.encode())
        return block_hash.hexdigest()

    def print_block(self):
        print("Transactions : {}".format(self.transactions))
        print("Timestamp : {}".format(self.timestamp))
        print("The previous blocks's hash : {}".format(self.previous_hash))
        print("Block's hash : {}".format(self.hash))
