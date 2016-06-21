from rest_framework import serializers


class VotingTotalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    politic_party = serializers.CharField()
    total_votes = serializers.CharField()


class VotingData(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    vote_date = serializers.CharField()
    voting_totals = serializers.ListField(
        child=VotingTotalSerializer()
    )
    citizen_participation = serializers.CharField()
    total_votes = serializers.FloatField()


class Voting(serializers.Serializer):
    voting = VotingData()
