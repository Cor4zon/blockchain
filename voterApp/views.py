import json

from django.http import Http404, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from backend.Transaction import Transaction
from backend.models import Voter
from backend.views import blockchain, new_transaction
from backend.repository.repository import VoterService

@csrf_exempt
def vote(request):
    if request.method != 'POST':
        raise Http404

    data = json.loads(request.body.decode())

    voting_id = data["voting_id"]
    pubkey = data["pubkey"]
    privkey = data["privkey"]
    choice = data["choice"]

    try:
        voter = Voter.objects.filter(pubkey=pubkey)[0]
        voter_id = voter.id
        voter_voteFor = voter.voteFor_id
        print(f'V: {voter_voteFor}')

        if (voter_voteFor != None):
            print("you have already voted")
            return HttpResponseBadRequest

        transaction = Transaction(pubkey, privkey, voting_id, choice)
        signature = transaction.sign_transaction()
        result = new_transaction(request, {'voting_id': voting_id, 'voter_pubkey': pubkey, 'choice': choice, 'signature': signature})
        if result[1] == 201:
            print(f'transaction result: {result[1]}')
            VoterService.update(voter_id, {'voteFor_id': choice})

        # blockchain.submit_transaction(voter_id, pubkey, choice, signature)

    except IndexError:
        # TODO: сделать кастомную ошибку
        print("incorrect keys")
        raise Http404

    return JsonResponse(data)

