from rest_framework import serializers


class CandidatesSerializer(serializers.Serializer):
    candidato_id = serializers.IntegerField()
    id_partido = serializers.IntegerField()
    nombre = serializers.CharField(required=False)
    nombre_partido = serializers.CharField()
    photo_url = serializers.URLField()
    logo_partido = serializers.URLField()
    total_votes = serializers.IntegerField(required=False)
    propuestas = serializers.ListField(
        child=serializers.CharField()
    )


class VotingData(serializers.Serializer):
    idvotacion = serializers.IntegerField()
    tipo = serializers.CharField()
    cadidatos = serializers.ListField(
        child=CandidatesSerializer()
    )
    participacion_ciudadana = serializers.FloatField(required=False)
    listanominal = serializers.IntegerField(required=False)
    votos_totales = serializers.IntegerField(required=False)


class Voting(serializers.Serializer):
    votacion = VotingData()
