from django.contrib import admin
from django.urls import path, include, re_path

from aboutUs.views import AboutUsHomepage, AvaliablePositions, SuscribeUserSVModelAdd, UserSendCVModelAdd
from work.views import WorkPage, WorkDetail

urlpatterns = [
    path('',AboutUsHomepage.as_view(), name='aboutUs'),#Приложение aboutUs
    path('avaliablePositions/',AvaliablePositions.as_view(),name='avaliablePositions'),#Страница вакансии
    path('SuscribeUserSVModelAdd/',SuscribeUserSVModelAdd.as_view(),name='SuscribeUserSVModelAdd'),#Страница обработка формы подписка на вакансии
    path('UserSendCVModelAdd/',UserSendCVModelAdd.as_view(),name='UserSendCVModelAdd'),#Страница обработка формы отправка резюме
]