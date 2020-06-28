from django.urls import path
from .views import *

urlpatterns = [
    path('participants/', ParticipantsList.as_view()),
    path('by_message/', TournamentByMsg.as_view())
]
