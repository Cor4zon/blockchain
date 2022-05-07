from backend.Transaction import Transaction

from backend.views import new_transaction


def vote(voter_pubkey, voter_privkey, voting_id, option_pubkey):
    transaction = Transaction(voter_pubkey, voter_privkey, voting_id, option_pubkey)
    signature = transaction.sign_transaction()
    new_transaction(None, {'voter_pubkey': voter_pubkey, 'option_pubkey': option_pubkey, 'voting_id': voting_id, 'signature': signature})
