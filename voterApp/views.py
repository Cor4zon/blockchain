import json

from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backend.Transaction import Transaction
from backend.models import Voter
from backend.views import blockchain


@csrf_exempt
def vote(request):
    if request.method != 'POST':
        raise Http404

    data = json.loads(request.body.decode())

    pubkey = data["pubkey"]
    privkey = data["privkey"]
    choice = data["choice"]

    try:
        voter_id = Voter.objects.filter(pubkey=pubkey)[0].id

        print(pubkey, privkey, choice, voter_id)
        transaction = Transaction(pubkey, privkey, voter_id, choice)
        signature = transaction.sign_transaction()
        blockchain.submit_transaction(voter_id, pubkey, choice, signature)

    except IndexError:
        # TODO: сделать кастомную ошибку
        print("incorrect keys")
        raise Http404

    return JsonResponse(data)

