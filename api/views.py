from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import Voting
import json
import requests


class VoteView(APIView):
    """
    Returns all the data of the voting in a JSON.
    """
    def get(self, request):
        # Receive json data from elixir server and parse to dict

        votes_data = requests.get('https://candidatos-d9e51.firebaseio.com/.json').json()  #Firebase
        candidate_votes = requests.get('http://52.40.75.90/api/0.1/votes/')    #Elixir
        candidate_votes_data = candidate_votes.json()['data']
        total_votes = 0

        for candidate_id, votes in candidate_votes_data.items():
            for candidate in votes_data['votacion']['cadidatos']:
                if candidate['candidato_id'] == candidate_id:
                    candidate['total_votes'] = votes
            total_votes += votes

        votes_data['votacion']['votos_totales'] = total_votes
        votes_data['votacion']['participacion_ciudadana'] = (total_votes * 100) / votes_data['votacion']['listanominal']

        votes_serializer = Voting(data=votes_data)

        if votes_serializer.is_valid():
            return Response(votes_serializer.data)

        content = {'Formato invalido': votes_serializer.errors}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
