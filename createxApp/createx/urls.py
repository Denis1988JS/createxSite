from django.contrib import admin
from django.urls import path, include, re_path

from .views import Homepage, AddUserSubscribe, addDiscussForUser

urlpatterns = [
    path('', Homepage.as_view(), name="home"),#Главная страница сайта
    path('addSubscribe/', AddUserSubscribe.as_view(), name='addUserSubscribe'),  # Обработчик UserSubscribeForm
    path('addDiscuss/',addDiscussForUser,name ='addDiscuss'),#Обработчик DiscussForUserForm
]