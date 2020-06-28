from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status

from .models import *
from .serializers import *

class EmbedList(ListAPIView):
    queryset = EmbedPlannerModel.objects.all()
    serializer_class = EmbedPlannerSerializer

class EmbedUpdate(APIView):
    def post(self, request):
        try:
            print(request.data)
            embed_planner_id = request.data["id"]
            embed_planner = EmbedPlannerModel.objects.get(id=embed_planner_id)
            if "is_done" in request.data:
                embed_planner.is_done = request.data["is_done"]
            if "message_id" in request.data:
                embed_planner.embed.message_id = request.data["message_id"]
                embed_planner.embed.save()
            embed_planner.save()
            return Response(status = status.HTTP_200_OK)
        except:
            raise
            return Response(status = status.HTTP_400_BAD_REQUEST)