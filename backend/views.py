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
    :param transaction_data: format({'voting_id': voting_id,'voter_pubkey': pubkey1, 'option_pubkey': pubkey3, 'signature': signature01})
    :return:
    """
    values = transaction_data
    print(f'values: {values}')

    required = ['voting_id', 'voter_pubkey', 'choice', 'signature']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    transaction_result = blockchain.submit_transaction(values['voting_id'], values['voter_pubkey'], values['choice'],
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
blockchain.transactions = [
    {
        "voting_id": 10,
        "voter_pubkey": "30819f300d06092a864886f70d010101050003818d0030818902818100d22878abdd0cfad53a7dada3b80ddfb4b70b91742a48332aadcb7b86d9e123d91e6f7488625188050a0f290584a9414c8433901b384b499318a0abdbc346261e58f20f612763d71630991ed622f8bd5ecee78e230ce9b0a878248bfc6e2a90ea22e002a2bdc4777fba22dd0a83030f2055752ef7d3f7a7cf7d5ef4dac646909f0203010001",
        "choice": 17
    },
{
        "voting_id": 10,
        "voter_pubkey": "30819f300d06092a864886f70d010101050003818d0030818902818100d22878abdd0cfad53a7dada3b80ddfb4b70b91742a48332aadcb7b86d9e123d91e6f7488625188050a0f290584a9414c8433901b384b499318a0abdbc346261e58f20f612763d71630991ed622f8bd5ecee78e230ce9b0a878248bfc6e2a90ea22e002a2bdc4777fba22dd0a83030f2055752ef7d3f7a7cf7d5ef4dac646909f0203010001",
        "choice": 17
    },
{
        "voting_id": 10,
        "voter_pubkey": "30819f300d06092a864886f70d010101050003818d0030818902818100d22878abdd0cfad53a7dada3b80ddfb4b70b91742a48332aadcb7b86d9e123d91e6f7488625188050a0f290584a9414c8433901b384b499318a0abdbc346261e58f20f612763d71630991ed622f8bd5ecee78e230ce9b0a878248bfc6e2a90ea22e002a2bdc4777fba22dd0a83030f2055752ef7d3f7a7cf7d5ef4dac646909f0203010001",
        "choice": 17
    },
{
        "voting_id": 10,
        "voter_pubkey": "30819f300d06092a864886f70d010101050003818d0030818902818100d22878abdd0cfad53a7dada3b80ddfb4b70b91742a48332aadcb7b86d9e123d91e6f7488625188050a0f290584a9414c8433901b384b499318a0abdbc346261e58f20f612763d71630991ed622f8bd5ecee78e230ce9b0a878248bfc6e2a90ea22e002a2bdc4777fba22dd0a83030f2055752ef7d3f7a7cf7d5ef4dac646909f0203010001",
        "choice": 17
    },
{
        "voting_id": 10,
        "voter_pubkey": "30819f300d06092a864886f70d010101050003818d0030818902818100d22878abdd0cfad53a7dada3b80ddfb4b70b91742a48332aadcb7b86d9e123d91e6f7488625188050a0f290584a9414c8433901b384b499318a0abdbc346261e58f20f612763d71630991ed622f8bd5ecee78e230ce9b0a878248bfc6e2a90ea22e002a2bdc4777fba22dd0a83030f2055752ef7d3f7a7cf7d5ef4dac646909f0203010001",
        "choice": 17
    },
{
        "voting_id": 10,
        "voter_pubkey": "30819f300d06092a864886f70d010101050003818d0030818902818100d22878abdd0cfad53a7dada3b80ddfb4b70b91742a48332aadcb7b86d9e123d91e6f7488625188050a0f290584a9414c8433901b384b499318a0abdbc346261e58f20f612763d71630991ed622f8bd5ecee78e230ce9b0a878248bfc6e2a90ea22e002a2bdc4777fba22dd0a83030f2055752ef7d3f7a7cf7d5ef4dac646909f0203010001",
        "choice": 17
    },
{
        "voting_id": 10,
        "voter_pubkey": "30819f300d06092a864886f70d010101050003818d0030818902818100d22878abdd0cfad53a7dada3b80ddfb4b70b91742a48332aadcb7b86d9e123d91e6f7488625188050a0f290584a9414c8433901b384b499318a0abdbc346261e58f20f612763d71630991ed622f8bd5ecee78e230ce9b0a878248bfc6e2a90ea22e002a2bdc4777fba22dd0a83030f2055752ef7d3f7a7cf7d5ef4dac646909f0203010001",
        "choice": 17
    },
{
        "voting_id": 10,
        "voter_pubkey": "30819f300d06092a864886f70d010101050003818d0030818902818100d22878abdd0cfad53a7dada3b80ddfb4b70b91742a48332aadcb7b86d9e123d91e6f7488625188050a0f290584a9414c8433901b384b499318a0abdbc346261e58f20f612763d71630991ed622f8bd5ecee78e230ce9b0a878248bfc6e2a90ea22e002a2bdc4777fba22dd0a83030f2055752ef7d3f7a7cf7d5ef4dac646909f0203010001",
        "choice": 17
    },
{
        "voting_id": 10,
        "voter_pubkey": "30819f300d06092a864886f70d010101050003818d0030818902818100d22878abdd0cfad53a7dada3b80ddfb4b70b91742a48332aadcb7b86d9e123d91e6f7488625188050a0f290584a9414c8433901b384b499318a0abdbc346261e58f20f612763d71630991ed622f8bd5ecee78e230ce9b0a878248bfc6e2a90ea22e002a2bdc4777fba22dd0a83030f2055752ef7d3f7a7cf7d5ef4dac646909f0203010001",
        "choice": 18
    },
{
        "voting_id": 10,
        "voter_pubkey": "30819f300d06092a864886f70d010101050003818d0030818902818100d22878abdd0cfad53a7dada3b80ddfb4b70b91742a48332aadcb7b86d9e123d91e6f7488625188050a0f290584a9414c8433901b384b499318a0abdbc346261e58f20f612763d71630991ed622f8bd5ecee78e230ce9b0a878248bfc6e2a90ea22e002a2bdc4777fba22dd0a83030f2055752ef7d3f7a7cf7d5ef4dac646909f0203010001",
        "choice": 18
    }
        ]


print(blockchain)
print(blockchain.transactions)
