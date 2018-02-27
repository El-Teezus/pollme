from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

#get models
from ..models import Question, Choice

#get serializers
from .serializers import (
    QuestionListSerializer
)

class QuestionListAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer

    # def get(self, request, format=None):
    #     """
    #     This should list all questions and their choices
    #     Feel free to use DRF generic class based views
    #     Otherwise it subclasses APIView
    #     """
    #     pass

    # def post(self, request, format=None):
    #     """nothing required for lab 5"""
    #     pass

    def put(self, request, format=None):
        """nothing required for lab 5"""
        pass

    def delete(self, request, format=None):
        """nothing required for lab 5"""
        pass
