from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from createx.models import AskFromUser, UserSubscribe, DiscussForUser
from news.models import NewsModel, NewsCommentsModefl
from services.models import OurServices, ourOfferServices
from work.models import OurWork
from .serializers import OurServicesSerializer, OurServicesDetailSerializer, NewsModelSerializer, AskFromUserSerializer, UserSubscribeSerializer, \
    DiscussForUserSerializer, OurWorkSerializer, OurOfferServicesSerializer, NewsCommentsModeflSerializer
from rest_framework import generics

#Представление - оферты- список к сервису - ourOfferServices
class OurOfferServicesApiView(generics.ListAPIView):
    queryset = ourOfferServices.objects.all()
    serializer_class = OurOfferServicesSerializer
class OurOfferServicesApiViewDetail(generics.RetrieveAPIView):
    queryset = ourOfferServices.objects.all()
    serializer_class = OurOfferServicesSerializer




#Все для OurServices -----------------------------------------------
#Представление все услуги модель OurServices - OurServicesSerializer
class OurServicesApiView(generics.ListAPIView ):
    queryset = OurServices.objects.filter(is_active=True)
    serializer_class = OurServicesSerializer

#Представление детально услуга модель OurServices - OurServicesSerializer
class OurServicesApiViewDetail(generics.RetrieveAPIView):
    queryset = OurServices.objects.filter(is_active=True)
    serializer_class = OurServicesDetailSerializer




#Все для модели NewsModel ------------------------------------------------
#Представление все новости модель NewsModel - NewsModelSerializer
class NewsModelApiView(generics.ListAPIView):
    queryset = NewsModel.objects.filter(is_published=True)
    serializer_class = NewsModelSerializer

#Представление детально новость модель NewsModel - NewsModelSerializer
class NewsModelApiViewDetail(generics.RetrieveAPIView ):
    queryset = NewsModel.objects.filter(is_published=True)
    serializer_class = NewsModelSerializer

#Добавление комментариев к новостям
class NewsCommentsModeflAdd(generics.ListCreateAPIView):
    queryset = NewsCommentsModefl.objects.filter(is_published=True)
    serializer_class = NewsCommentsModeflSerializer


#Все для модели - OurWork------------------------------------------------
#Представление все услуги модель - OurWork
class OurWorkApiView(generics.ListAPIView):
    queryset = OurWork.objects.all()
    serializer_class = OurWorkSerializer

#Представление услуга модель - OurWork - детально
class OurWorkApiViewDetail(generics.RetrieveAPIView):
    queryset = OurWork.objects.all()
    serializer_class = OurWorkSerializer


#Представления - те модели - которые в приложении - добавляет пользователь через форму - с методом POST

class AskFromUserViewAdd(generics.ListCreateAPIView):
    #Представление - AskFromUser - добавить/отобразить вопросы от пользователей
    queryset = AskFromUser.objects.all()
    serializer_class = AskFromUserSerializer

class UserSubscribeApiView(generics.ListCreateAPIView):
    # Представление - UserSubscribe - добавить/отобразить Подписчики сайта
    queryset = UserSubscribe.objects.all()
    serializer_class = UserSubscribeSerializer

class DiscussForUserApiView(generics.ListCreateAPIView):
    # Представление - UserSubscribe - добавить/отобразить Подписчики сайта
    queryset = DiscussForUser.objects.all()
    serializer_class = DiscussForUserSerializer


























