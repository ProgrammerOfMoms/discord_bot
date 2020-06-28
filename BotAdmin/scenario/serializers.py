from rest_framework import serializers
from .models import *


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenarioModel
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    scenario = ScenarioSerializer()
    class Meta:
        model = QuestionModel
        fields = "__all__"

class ScenarioDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = ScenarioModel
        fields = "__all__"