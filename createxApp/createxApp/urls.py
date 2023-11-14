"""
URL configuration for createxApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from createxApp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),#Приложение ckeditor
    path('', include('createx.urls')),#Маршруты из приложения createx

    path('services/', include('services.urls')),#Маршруты из приложения services
    path('work/', include('work.urls')),#Маршруты из приложения work
    path('aboutUs/', include('aboutUs.urls')),#Маршруты из приложения work
    path('news/', include('news.urls')),#Маршруты из приложения news
]

#Добавление графических файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)