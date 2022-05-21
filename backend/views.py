from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from backend.Blockchain import Blockchain
from backend.models import VotingOption, Voter
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def get_transactions(request):
    return JsonResponse({"transactions": blockchain.transactions})

@csrf_exempt
def get_blockchain(request):
    return JsonResponse({"blockchain": blockchain.chain})




def get_results(request, pk):
    voting_id = pk
    voting_options = VotingOption.objects.filter(voting_id=voting_id)
    voters = Voter.objects.all()
    voting_result = {}

    for i in range(len(voting_options)):
        voting_result[voting_options[i].id] = 0

    for i in range(len(voters)):
        voteFor = voters[i].voteFor_id
        if voteFor in voting_result:
            voting_result[voteFor] += 1

    print(voting_result)
    return JsonResponse(voting_result)


blockchain = Blockchain()
