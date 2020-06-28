from rest_framework import serializers
from .models import *

from tournament.serializers import TournamentSerializer
from embed.serializers import EmbedSerializer
from scenario.serializers import ScenarioDetailSerializer

class UserModelSerializer(serializers.ModelSerializer):
    tournaments = TournamentSerializer(many=True)
    scenario = ScenarioDetailSerializer()
    class Meta:
        model = UserModel
        fields = "__all__"

class UserReactionSerializer(serializers.ModelSerializer):
    embed = EmbedSerializer()
    class Meta:
        model = UserReactionModel
        fields = "__all__"