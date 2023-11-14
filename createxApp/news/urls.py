from django.contrib import admin
from django.urls import path, include, re_path

from news.views import NewsPage, NewsDetail, AddComment

urlpatterns = [
    path('',NewsPage.as_view(), name='news'),#Главная страница - news
    path('<slug:slug>',NewsDetail.as_view(), name='newsDetail' ), #Страница - новость детально
    path('add-comment/<int:pk>/',AddComment.as_view(), name='AddComment') #Страница - добавить комментарий
]