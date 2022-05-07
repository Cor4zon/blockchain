from rest_framework import serializers
from backend.models import Voting, VotingOption, Voter


class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = '__all__'


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = '__all__'


class VotingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotingOption
        fields = '__all__'