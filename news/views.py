from django.shortcuts import render
from rest_framework import viewsets,generics
from news.api.serializer import ArticleSerializer,JournalistSerializer
from news.models import Article,Journalist

# Create your views here.

class ArticleAPIGeneric(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleAPIViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class= ArticleSerializer

class JournalistAPIViewset(viewsets.ModelViewSet):
    queryset = Journalist.objects.all()
    serializer_class = JournalistSerializer