from rest_framework import serializers
from .models import *

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentModel
        fields = "__all__"