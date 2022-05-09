from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from backend.models import Voting, Voter, VotingOption
from backend.repository.repository import VotingService, VoterService, VotingOptionService
from backend.serializers import VotingSerializer, VoterSerializer, VotingOptionSerializer


class VotingList(APIView):
    """
    List all votings, or create a new voting.
    """
    def get(self, request, format=None):
        votings = VotingService.read_all()
        serializer = VotingSerializer(votings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        new_voting = request.data
        VotingService.create(new_voting)
        serializer = VotingSerializer(new_voting)
        return Response(serializer.data)


class VotingDetail(APIView):
    """
    Retrieve, update or delete a voting instance.
    """
    def get_object(self, pk):
        try:
            return VotingService.read(pk)
        except Voting.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        voting = self.get_object(pk)
        serializer = VotingSerializer(voting)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        new_voting = request.data
        VotingService.update(pk, new_voting)
        serializer = VotingSerializer(data=new_voting)

        if serializer.is_valid():
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        VotingService.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class VoterList(APIView):
    """
    List all voters, or create a new voter.
    """
    def get(self, request, format=None):
        voters = VoterService.read_all()
        serializer = VoterSerializer(voters, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VoterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoterDetail(APIView):
    """
    Retrieve, update or delete a voter instance.
    """
    def get_object(self, pk):
        try:
            return VoterService.read(pk)
        except Voter.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        voter = self.get_object(pk)
        serializer = VoterSerializer(voter)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        new_voter = request.data
        VoterService.update(pk, new_voter)
        serializer = VoterService(data=new_voter)

        if serializer.is_valid():
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        voter = self.get_object(pk)
        VoterService.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class VotingOptionList(APIView):
    def get(self, request, format=None):
        voting_options = VotingOptionService.read_all()
        serializer = VotingOptionSerializer(voting_options, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VotingOptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VotingOptionDetail(APIView):
    def get_object(self, pk):
        try:
            return VotingOption.objects.get(pk=pk)
        except VotingOption.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        voting_option = self.get_object(pk)
        serializer = VotingOptionSerializer(voting_option)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        voting_option = self.get_object(pk)
        serializer = VotingOptionSerializer(voting_option, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        voting_option = self.get_object(pk)
        voting_option.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
