from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import NewsModel
from services.models import OurServices
from .serializers import OurServicesSerializer, OurServicesDetailSerializer, NewsModelSerializer
from rest_framework import generics

#Представление все услуги модель OurServices - OurServicesSerializer
class OurServicesApiView(generics.ListAPIView ):
    queryset = OurServices.objects.filter(is_active=True)
    serializer_class = OurServicesSerializer

#Представление детально услуга модель OurServices - OurServicesSerializer
class OurServicesApiViewDetail(generics.RetrieveAPIView):
    queryset = OurServices.objects.filter(is_active=True)
    serializer_class = OurServicesDetailSerializer

#Представление все новости модель NewsModel - NewsModelSerializer
class NewsModelApiView(generics.ListAPIView):
    queryset = NewsModel.objects.filter(is_published=True)
    serializer_class = NewsModelSerializer

#Представление детально новость модель NewsModel - NewsModelSerializer
class NewsModelApiViewDetail(generics.RetrieveAPIView ):
    queryset = NewsModel.objects.filter(is_published=True)
    serializer_class = NewsModelSerializer