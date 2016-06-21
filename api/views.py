from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import Voting
import json


class VoteView(APIView):
    """
    Returns all the data of the voting in a JSON.
    """
    def get(self, request):
        # Receive json data from elixir server and parse to dict
        votes_data = {
            'voting':{
                            'id': 10,
                            'type': 'Diputados',
                            'vote_date': '2016-11-10',
                            'voting_totals': [
                            {
                                'id': 234,
                                'politic_party': 'JUJIU',
                                'total_votes': 200,
                                'candidate_name': 'Fabiola'
                            },
                            {
                                'id': 43,
                                'politic_party': 'JUJIU',
                                'total_votes': 200,
                                'candidate_name': 'Joaquin'
                            }
                            ],
                            'citizen_participation': 400,
                            'total_votes': 123
                    }
        }
        votes_serializer = Voting(data=votes_data)

        if votes_serializer.is_valid():
            return Response(votes_serializer.data)

        content = {'Formato invalido': votes_serializer.errors}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
