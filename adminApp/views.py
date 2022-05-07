from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from backend.models import Voting, Voter, VotingOption
from backend.serializers import VotingSerializer, VoterSerializer, VotingOptionSerializer


class VotingList(APIView):
    """
    List all votings, or create a new voting.
    """
    def get(self, request, format=None):
        votings = Voting.objects.all()
        serializer = VotingSerializer(votings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VotingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VotingDetail(APIView):
    """
    Retrieve, update or delete a voting instance.
    """
    def get_object(self, pk):
        try:
            return Voting.objects.get(pk=pk)
        except Voting.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        voting = self.get_object(pk)
        serializer = VotingSerializer(voting)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        voting = self.get_object(pk)
        serializer = VotingSerializer(voting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        voting = self.get_object(pk)
        voting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
