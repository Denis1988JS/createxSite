from rest_framework.response import Response
from  rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from createx.models import AskFromUser, UserSubscribe, DiscussForUser
from news.models import NewsModel, NewsCommentsModefl
from services.models import OurServices, ourOfferServices
from work.models import OurWork, PhotoSliderWork, OurWorkData



#Сериализаторы для страницы OurWork - наши работы + выполненная работа детльно
#1.Вывод - Списка работ + объект проекта + вид услуги + слайдер к выполненной работе + описание работы
#Сериализатор - описание работы OurWorkData
class OurWorkDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurWorkData
        fields = "__all__"
#Сериализатор - слайдер модели PhotoSliderWork
class PhotoSliderWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoSliderWork
        fields = "__all__"
#Сериализатор - выполненные работы/услуги
class OurWorkSerializer(serializers.ModelSerializer):
    #Чтобы показать не id - связанных моделей а имена моделей
    objectID = serializers.SlugRelatedField(slug_field="name", read_only=True)
    workServicesID = serializers.SlugRelatedField(slug_field="title", read_only=True)
    photoSlider = PhotoSliderWorkSerializer(many=True)
    workData = OurWorkDataSerializer(many=True)
    class Meta:
        model = OurWork
        fields = "__all__"


#Сериализаторы для страницы OurServices - наши услуги + услуга детально
#Сериализатор - оферты к сервису - ourOfferServices
class OurOfferServicesSerializer(serializers.ModelSerializer):
    servicesID = serializers.SlugRelatedField(slug_field="title", read_only=True)
    class Meta:
        model = ourOfferServices
        fields = "__all__"

#Сериализатор модели OurServices - наши услуги
class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields = "__all__"

#Сериализатор модели OurServices - наша услуга детально
class OurServicesDetailSerializer(serializers.ModelSerializer):
    offers = OurOfferServicesSerializer(many=True)#Получить все оферты к сервису(через  related_name)
    works = OurWorkSerializer(many=True)#Получить все работы к сервису(через  related_name)
    class Meta:
        model = OurServices
        fields = "__all__"

#Сериализаторы для страницы NewsModel - все новости + новость
#Где одна новость - комментарии + добавить комментарий

class NewsCommentsModeflSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCommentsModefl
        fields = "__all__"
    def get(self, request):
        comments = NewsCommentsModefl.objects.filter(is_published=True)
        return Response({'comments': comments})

    def post(self, request):
        serializer = NewsCommentsModeflSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'comments': serializer.data})
#Сериализатор модели NewsModel - новости
class NewsModelSerializer(serializers.ModelSerializer):
    news = NewsCommentsModeflSerializer(many=True)
    categoryID = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = NewsModel
        fields = "__all__"

#Сериализатор модели NewsModel - новость детально
class NewsModelDetailSerializer(serializers.ModelSerializer):
    # Чтобы показать не id - связанных моделей а имена моделей
    categoryID = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = NewsModel
        fields = "__all__"


#-----------------------------------------------------------#
#Сериализаторы для моделей - из форм сайта которые заносят пользователи

#Сериализатор для модели AskFromUser- Вопросы от пользоватей из данные формы

class AskFromUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AskFromUser
        fields = "__all__"
    def get(self,request):
        users = AskFromUser.objects.all()
        return Response({'data': users})
    def post(self, request):
        serializer = AskFromUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data':serializer.data})


#Сериализатор модели - UserSubscribe - подписчики
class UserSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscribe
        fields = ('userEmail',)
    def get(self,request):
        users = UserSubscribe.objects.all()
        return Response({'data': users})
    def post(self, request):
        serializer = UserSubscribeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data':serializer.data})

#Сериализатор модели - DiscussForUser - Обсуждение от пользователей
class DiscussForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussForUser
        fields = ('userName','phoneNumberUser','emailUser','discussContent','userAgree')
    def get(self,request):
        users = DiscussForUser.objects.all()
        return Response({'data': users})
    def post(self, request):
        serializer = DiscussForUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data':serializer.data})

