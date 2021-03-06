import binascii
from collections import OrderedDict

from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Transaction:
    def __init__(self, voter_pubkey, voter_privkey, voting_id, choice):
        self.voter_pubkey = voter_pubkey
        self.voter_privkey = voter_privkey
        self.voting_id = voting_id
        self.choice = choice

    def to_dict(self):
        return OrderedDict({
                            'voting_id': self.voting_id,
                            'voter_pubkey': self.voter_pubkey,
                            'choice': self.choice })

    def sign_transaction(self):
        """
        Sign transaction with private key
        """
        private_key = RSA.importKey(binascii.unhexlify(self.voter_privkey))
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')
