from django.shortcuts import render
# from django.http import HttpResponse
import json

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView
from api import serializers,models


class ArticleListView(ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

class ArticleDetailView(RetrieveUpdateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
