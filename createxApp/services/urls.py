from django.contrib import admin
from django.urls import path, include, re_path

from services.views import ServicesPage, ServicesPageDetail

urlpatterns = [
    path('',ServicesPage.as_view(), name='services'),#Главная страница services - все услуги
    path('<slug:slug>', ServicesPageDetail.as_view(), name='services'),  # Страница описание услуги
]