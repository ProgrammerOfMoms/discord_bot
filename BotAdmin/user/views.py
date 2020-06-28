from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status

from .models import *
from embed.models import EmbedModel
from scenario.models import ScenarioModel
from tournament.models import TournamentModel
from .serializers import *
from scenario.serializers import QuestionSerializer

class UserList(ListAPIView):
    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()

class UserReactionCreate(APIView):
    def post(self, request):
        guild_id = request.data['guild_id']
        message_id = request.data['message_id']
        user_id = request.data['user_id']

        user = UserModel.objects.get_or_create(id=user_id)
        embed = EmbedModel.objects.get(message_id=message_id)
        user_reaction = UserReactionModel.objects.create(guild_id=guild_id, user=user, embed=embed)
        serializer = UserReactionSerializer(user_reaction)
        return Response(data=serializer.data, status = status.HTTP_200_OK)

class UserRegister(APIView):
    def post(self, request):
        t_id = request.data["tournament_id"]
        user_id = request.data["user_id"]
        tournament = TournamentModel.objects.get(id=t_id)
        user = UserModel.objects.get(id=user_id)
        user.tournaments.add(tournament)
        user.save()
        return Response(status=status.HTTP_200_OK)

class UserBindScenario(APIView):
    def post(self, request):
        s_id = request.data['scenario_id']
        u_id = request.data['user_id']
        user = UserModel.objects.get(id=u_id)
        scenario = ScenarioModel.objects.get(id=s_id)
        user.scenario = scenario
        user.next_question = 1
        user.save()
        return Response(status = status.HTTP_200_OK)

class UserScenarioQuestion(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        user = UserModel.objects.get(id=user_id)
        n_msg = user.next_question
        if n_msg is not None:
            try:
                qs = QuestionSerializer(user.scenario.questions, many=True)
                q = qs.data[n_msg]["q"]
                print(q)
                user.next_question += 1
                user.save()
                return Response(data={"q": q}, status=status.HTTP_200_OK)
            except:
                q = "Вы успешно зарегистрированы!"
                user.next_question += 1
                user.save()
                return Response(data={"q": q}, status=status.HTTP_200_OK)
        else:
            return Response(data={"q": None}, status=status.HTTP_200_OK)

class UserProcessMsg(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        content = request.data['content']
        user = UserModel.objects.get(id=user_id)
        print(user.scenario.name)
        qs = QuestionSerializer(user.scenario.questions, many=True)
        if user.scenario.name == "Первичная регистрация":
            n_question = user.next_question - 1
            if n_question >= len(qs.data):
                user.scenario = None
                user.next_question = None
                user.save()
                return Response(status = status.HTTP_200_OK)
            if n_question == 0:
                user.sc_name = content
                user.save()
                return Response(status=status.HTTP_200_OK)
            elif n_question == 1:
                user.challonge_account = content
                user.save()
                return Response(status=status.HTTP_200_OK)
            elif n_question == 2:
                user.ranked_ftw = content
                user.save()
                return Response(status=status.HTTP_200_OK)
            elif n_question == 3:
                user.max_ranked = int(content)
                user.save()
                return Response(status=status.HTTP_200_OK)
            elif n_question == 4:
                user.rating_games_count = int(content)
                user.save()
                return Response(status=status.HTTP_200_OK)
            elif n_question == 5:
                user.rasa = content
                user.save()
                return Response(status=status.HTTP_200_OK)
            elif n_question == 6:
                user.team = content
                user.save()
                return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)