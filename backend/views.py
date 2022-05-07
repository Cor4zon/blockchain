from collections import OrderedDict

from django.http import HttpResponse
from django.shortcuts import render
from backend.Blockchain import Blockchain
from backend.Transaction import Transaction

from backend.keys import *

def index(request):
    return render(request, "index.html", context={"chain": blockchain.chain})


def new_transaction(request, transaction_data):
    """

    :param request:
    :param transaction_data: format({'voter_pubkey': pubkey1, 'option_pubkey': pubkey3, 'signature': signature01})
    :return:
    """
    values = transaction_data
    print(f'values: {values}')

    required = ['voter_pubkey', 'option_pubkey', 'signature']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    transaction_result = blockchain.submit_transaction(values['voter_pubkey'], values['option_pubkey'],
                                                       values['signature'])

    if transaction_result == False:
        response = {'message': 'Invalid Transaction!'}
        print(response)
        return HttpResponse(f'<h1>{response}</h1>'), 406
    else:
        response = {'message': 'Transaction will be added to Block ' + str(transaction_result)}
        print(response)
        return HttpResponse(f'<h1>{response}</h1>'), 201


def get_transactions(request):
    pass


def full_chain(request):
    pass


def mine(request):
    # if (request.method != 'GET'):
    #     return

    last_block = blockchain.chain[-1]
    nonce = blockchain.proof_of_work()


    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(nonce, previous_hash)

    response = {
        'message': "New Block Forged",
        'block_number': block['block_number'],
        'transactions': block['transactions'],
        'nonce': block['nonce'],
        'previous_hash': block['previous_hash'],
    }


blockchain = Blockchain()
print(blockchain.chain)


transaction1 = Transaction(pubkey1, privkey1, pubkey3)
transaction01 = OrderedDict({'voter_pubkey': pubkey1,
                           'option_pubkey': pubkey3})

transaction2 = Transaction(pubkey2, privkey2, pubkey3)
transaction02 = OrderedDict({'voter_pubkey': pubkey1,
                           'option_pubkey': pubkey3})


signature01 = transaction1.sign_transaction()

new_transaction(None, {'voter_pubkey': pubkey1, 'option_pubkey': pubkey3, 'signature': signature01})
new_transaction(None, {'voter_pubkey': pubkey2, 'option_pubkey': pubkey3, 'signature': transaction2.sign_transaction()})



print(f'blockchain: {blockchain.chain}')
mine(None)
print(f'blockchain: {blockchain.chain}')