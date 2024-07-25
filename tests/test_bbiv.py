
import unittest
from bbiv import BlockchainIdentityVerification

class TestBBIV(unittest.TestCase):
    def setUp(self):
        self.bbiv = BlockchainIdentityVerification()

    def test_create_block(self):
        previous_block = self.bbiv.get_previous_block()
        proof = self.bbiv.proof_of_work(previous_block['proof'])
        block = self.bbiv.create_block(proof, self.bbiv.hash(previous_block))
        self.assertEqual(block['index'], 2)

    def test_is_chain_valid(self):
        self.assertTrue(self.bbiv.is_chain_valid())

if __name__ == '__main__':
    unittest.main()
