from django.urls import path
from .views import *

urlpatterns = [
    path('', UserList.as_view()),
    path('reaction/', UserReactionCreate.as_view()),
    path('register/', UserRegister.as_view()),
    path('bind_scenario/', UserBindScenario.as_view()),
    path('scenario/next/', UserScenarioQuestion.as_view()),
    path('process/', UserProcessMsg.as_view()),
    path('create/', UserCreateView.as_view()),
]
