from rest_framework import serializers


class VotingTotalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    candidate_name = serializers.CharField(required=False)
    politic_party = serializers.CharField()
    total_votes = serializers.IntegerField()


class VotingData(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField()
    vote_date = serializers.CharField()
    voting_totals = serializers.ListField(
        child=VotingTotalSerializer()
    )
    citizen_participation = serializers.FloatField()
    total_votes = serializers.IntegerField()


class Voting(serializers.Serializer):
    voting = VotingData()
