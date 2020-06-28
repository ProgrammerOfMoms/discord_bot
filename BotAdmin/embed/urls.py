from django.urls import path
from .views import *

urlpatterns = [
    path('', EmbedList.as_view()),
    path('update/', EmbedUpdate.as_view())
]
