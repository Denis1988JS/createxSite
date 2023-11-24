from  rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from news.models import NewsModel
from services.models import OurServices

#Сериализатор модели OurServices - наши услуги

class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields = "__all__"

#Сериализатор модели OurServices - наша услуга детально
class OurServicesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields = "__all__"

#Сериализатор модели NewsModel - новости
class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = "__all__"

#Сериализатор модели NewsModel - новость детально

class NewsModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = "__all__"




