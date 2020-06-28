from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status

from .models import *
from .serializers import *

class ScenarioList(ListAPIView):
    serializer_class = ScenarioDetailSerializer
    queryset = ScenarioModel.objects.all()

class ScenarioByName(APIView):
    def post(self, request):
        name = request.data["name"]
        scenario = ScenarioModel.objects.get(name=name)
        serializer = ScenarioDetailSerializer(scenario)
        return Response(data=serializer.data, status = status.HTTP_200_OK)