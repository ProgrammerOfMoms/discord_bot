from rest_framework import serializers
from .models import *


class EmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmbedModel
        fields = "__all__"

class EmbedPlannerSerializer(serializers.ModelSerializer):
    embed = EmbedSerializer()
    class Meta:
        model = EmbedPlannerModel
        fields = "__all__"