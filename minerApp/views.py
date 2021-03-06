from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from backend.Blockchain import Blockchain
from backend.models import VotingOption, Voter

from Crypto.PublicKey import RSA
import Crypto
import binascii
from backend.views import blockchain




def get_transactions(request):
    pass


def full_chain(request):
    pass

@csrf_exempt
def mine(request):

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

    return JsonResponse(response)
