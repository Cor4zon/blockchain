from collections import OrderedDict

from django.http import HttpResponse
from django.shortcuts import render
from backend.Blockchain import Blockchain
from backend.Transaction import Transaction

from backend.keys import *

from Crypto.PublicKey import RSA
import Crypto
import binascii


def index(request):
    return render(request, "index.html", context={"chain": blockchain.chain})


def new_keys(request):
    random_gen = Crypto.Random.new().read
    private_key = RSA.generate(1024, random_gen)
    public_key = private_key.publickey()
    response = {
        'private_key': binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),
        'public_key': binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
    }

    print(private_key)
    print(public_key)

    return JsonResponse(response)


def new_transaction(request, transaction_data):
    """

    :param request:
    :param transaction_data: format({'voter_pubkey': pubkey1, 'option_pubkey': pubkey3, 'signature': signature01})
    :return:
    """
    values = transaction_data
    print(f'values: {values}')

    required = ['voting_id', 'voter_pubkey', 'option_pubkey', 'signature']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    transaction_result = blockchain.submit_transaction(values['voting_id'], values['voter_pubkey'], values['option_pubkey'],
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
