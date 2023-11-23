from  rest_framework.serializers import ModelSerializer
from rest_framework import serializers
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




