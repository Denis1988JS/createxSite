from django.contrib import admin
from django.urls import path, include, re_path
from contacts.views import ContactsView, AddContact

urlpatterns = [
    path('',ContactsView.as_view(), name='contacts'),#Страница приложения contacts
    path('AddContact/',AddContact.as_view(), name="AddContact")#Обработчик AddContact формы
]