from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status

from .models import *
from embed.models import EmbedModel
from .serializers import *
from user.serializers import UserModelSerializer

class ParticipantsList(APIView):
    def post(self, request):
        t_id = request.data["id"]
        tournament = TournamentModel.objects.get(id=t_id)
        users = UserModelSerializer(tournament.participants, many=True)
        print(users.data)
        return Response(data=users.data, status = status.HTTP_200_OK)

class TournamentByMsg(APIView):
    def get(self, request):
        pk = request.GET.get("message_id", None)
        if pk is not None:
            embed = EmbedModel.objects.get(message_id=pk)
            tournament = TournamentSerializer(embed.tournament)
            return Response(data=tournament.data, status= status.HTTP_200_OK)