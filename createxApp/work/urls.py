from django.contrib import admin
from django.urls import path, include, re_path

from work.views import WorkPage, WorkDetail

urlpatterns = [
    path('',WorkPage.as_view(), name='work'),#Главная страница work - все выполненные работы
    path('<slug:slug>',WorkDetail.as_view(), name='workDetail'),#Страница - услуга детально
]