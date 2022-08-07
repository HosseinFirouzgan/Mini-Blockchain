from Blocks import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, "0")
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_blocks_hash = self.chain[-1].hash
        new_block = Block(transactions, previous_blocks_hash)
        self.chain.append(new_block)
