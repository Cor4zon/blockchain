from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import viewsets

from backend.models import Voting, Voter, VotingOption
from backend.serializers import VotingSerializer, VoterSerializer, VotingOptionSerializer


@csrf_exempt
def voting_list(request):
    if request.method == 'GET':
        votings = Voting.objects.all()
        serializer = VotingSerializer(votings, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VotingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def voting_detail(request, pk):
    try:
        voting = Voting.objects.get(pk=pk)
    except Voting.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VotingSerializer(voting)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VotingSerializer(voting, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        voting.delete()
        return HttpResponse(status=204)