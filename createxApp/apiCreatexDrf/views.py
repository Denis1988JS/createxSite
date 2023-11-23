from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from services.models import OurServices
from .serializers import OurServicesSerializer,OurServicesDetailSerializer
from rest_framework import generics

#Представление все услуги модель OurServices - OurServicesSerializer
class OurServicesApiView(generics.ListCreateAPIView):
    queryset = OurServices.objects.filter(is_active=True)
    serializer_class = OurServicesSerializer

#Представление детально услуга модель OurServices - OurServicesSerializer
class OurServicesApiViewDetail(generics.RetrieveAPIView):
    queryset = OurServices.objects.filter(is_active=True)
    serializer_class = OurServicesDetailSerializer
