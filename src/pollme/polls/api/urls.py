"""
views.py
Lawrence Thompson
02/27/18
polls.api.urls conf
Takes in data from .views (in same package) and 
pushes it as a view using it's built in as_view().
"""
from django.urls import path

from .views import (
    QuestionListAPIView
)


app_name = "polls_api"
urlpatterns = [
    path('', QuestionListAPIView.as_view(), name='questions_list'),
]
