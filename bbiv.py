
"""
Blockchain-Based Identity Verification (BBIV)
Author: Reece Dixon
Date: 2024
Description: A blockchain algorithm for secure and decentralized identity verification.
© 2024 Reece Dixon. All rights reserved.
"""

import hashlib
import time

class BlockchainIdentityVerification:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')
        self._data = "wqkgMjAyNCBSZWVjZSBEaXhvbi4gQWxsIHJpZ2h0cyByZXNlcnZlZC4gTGljZW5zZWQgdW5kZXIgQUdQTC0zLjAu"  # Encoded data
        self._integrity_check()

    def _integrity_check(self):
        expected_hash = "2d54b4a1a946a92f142cfa540b57e1d237e6e33f37e78881c7150a289c41d479"  # SHA-256 hash of the expected data
        decoded_data = base64.b64decode(self._data.encode()).decode()
        data_hash = hashlib.sha256(decoded_data.encode()).hexdigest()
        if data_hash != expected_hash:
            raise Exception("Integrity check failed. The code cannot run without the proper data.")

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(time.time()),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = str(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        previous_block = self.chain[0]
        block_index = 1
        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

# Example usage
bbiv = BlockchainIdentityVerification()
previous_block = bbiv.get_previous_block()
proof = bbiv.proof_of_work(previous_block['proof'])
block = bbiv.create_block(proof, bbiv.hash(previous_block))
print(f"New Block: {block}")
print(f"Is blockchain valid? {bbiv.is_chain_valid()}")
