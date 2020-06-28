from django.urls import path
from .views import *

urlpatterns = [
    path("", ScenarioList.as_view()),
    path("by_name/", ScenarioByName.as_view())
]
