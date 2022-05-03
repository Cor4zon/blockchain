import binascii
import hashlib
import json
from collections import OrderedDict
from datetime import time

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

MINING_DIFFICULTY = 2


class Blockchain:
    def __init__(self):
        self.transactions = []
        self.chain = []
        self.nodes = set()
        self.create_block(0, '00')


    def register_node(self, node_url):
        pass

    def verify_transaction_signature(self, voter_pubkey, signature, transaction):
        public_key = RSA.importKey(binascii.unhexlify(voter_pubkey))
        verifier = PKCS1_v1_5.new(public_key)
        h = SHA.new(str(transaction).encode('utf8'))
        return verifier.verify(h, binascii.unhexlify(signature))

    def submit_transaction(self, voter_pubkey, option_pubkey, signature):
        """
        Add a transaction to transactions array if the signature verified

        :param voter_address:  voter public key
        :param option_number: option public key
        :param signature:
        :return:
        """
        transaction = OrderedDict({'voter_pubkey': voter_pubkey,
                                   'option_pubkey': option_pubkey})

        transaction_verification = self.verify_transaction_signature(voter_pubkey, signature, transaction)
        if transaction_verification:
            self.transactions.append(transaction)
            return len(self.chain) + 1
        else:
            return False

    def create_block(self, nonce, previous_hash):
        block = {'block_number': len(self.chain) + 1,
                # 'timestamp': time(),
                'transactions': self.transactions,
                'nonce': nonce,
                'previous_hash': previous_hash}

        # Reset the current list of transactions
        self.transactions = []

        self.chain.append(block)
        return block


    def hash(self, block):
        """
        Create a SHA-256 hash of a block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self):
        # Proof of work algorithm
        last_block = self.chain[-1]
        last_hash = self.hash(last_block)

        nonce = 0
        while self.valid_proof(self.transactions, last_hash, nonce) is False:
            nonce += 1

        return nonce

    def valid_proof(self, transactions, last_hash, nonce, difficulty=MINING_DIFFICULTY):
        # Check if a hash value satisfies the mining conditions.
        guess = (str(transactions) + str(last_hash) + str(nonce)).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:difficulty] == '0' * difficulty

    def valid_chain(self, chain):
        pass
