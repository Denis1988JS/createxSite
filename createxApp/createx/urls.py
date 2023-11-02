from django.contrib import admin
from django.urls import path, include, re_path

from .views import Homepage, AddUserSubscribe, addDiscussForUser,AddAsk

urlpatterns = [
    path('', Homepage.as_view(), name="home"),#Главная страница сайта
    path('addSubscribe/', AddUserSubscribe.as_view(), name='addUserSubscribe'),  # Обработчик UserSubscribeForm
    path('addDiscuss/',addDiscussForUser,name ='addDiscuss'),#Обработчик DiscussForUserForm
    path('askAdd/',AddAsk.as_view(),name ='addAsk'),#Обработчик AskFromUserForm
]