from django.db import models
from django.core.exceptions import ValidationError
from django.core import validators
import re
# Create your models here.
#Валидатор для полей с номером телефона
def ValidateNumberPhone(size):
    pattern = r"^\+?[123456789][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$"
    p = re.compile(pattern)
    rezult = p.search(size)
    if not rezult:
        raise ValidationError('Номер телефона в формате 81234567890 или +71234567890')


class HeaderContent(models.Model):
    #Модель заголовка сайта
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(max_length=1000, verbose_name='Содержание')
    img = models.ImageField(upload_to="header/%Y/%m/%d/", verbose_name='Фотография')
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = "Заголовок страницы"
        verbose_name_plural = "Заголовоки страниц"
class MainSliderModel(models.Model):
    #Модель главный слайдер
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.CharField(max_length=500, verbose_name='Содержание')
    imageSlider = models.ImageField(upload_to="mainSlider/%Y/%m/%d/", verbose_name='Фотография')
    isPublished = models.BooleanField(default=True, verbose_name='Опубликовать')
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = "Главный слайдер"
        verbose_name_plural = "Главный слайдер"

class OurCoreValues(models.Model):
    #Модель наши ценности
    titleCore = models.CharField(max_length=50, verbose_name='Название')
    contentCore = models.TextField(max_length=500, verbose_name='Содержание')
    coreIcon = models.ImageField(upload_to="coreValues/%Y/%m/%d/", verbose_name='Логотип')
    def __str__(self):
        return f'{self.titleCore}'
    class Meta:
        verbose_name = "Наша ценность"
        verbose_name_plural = "Наши ценности"

class OurPartners(models.Model):
    # Модель наши партнеры
    namePartners = models.CharField(max_length=30, verbose_name='Имя')
    slug = models.SlugField(max_length=35, verbose_name='url-partners')
    logo = models.ImageField(upload_to="ourPartners/%Y/%m/%d/", verbose_name='Логотип')
    def __str__(self):
        return f'{self.namePartners}'
    class Meta:
        verbose_name = "Наш партнер"
        verbose_name_plural = "Наши партнеры"

class AskFromUser(models.Model):
    #Вопросы от пользоватей + форма
    userName = models.CharField(max_length=100, verbose_name='Имя пользователя')
    phoneNumberUser = models.CharField(max_length=50, verbose_name='Номер телефона', validators=[
        ValidateNumberPhone], error_messages={'invalid':'Введите в формате 00x00 или 000x000'})
    askContent = models.TextField(max_length=5000, verbose_name='Вопрос от пользователя')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата вопроса')
    def __str__(self):
        return f'{self.userName}'
    class Meta:
        verbose_name = "Вопрос от пользователя"
        verbose_name_plural = "Вопросы от пользователей"

class UserSubscribe(models.Model):#+ форма для подписки в footer на всех страницах
    #Подписчики + форма для подписки в footer
    userEmail = models.EmailField(max_length=100, verbose_name='E-mail подписчика')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки')
    def __str__(self):
        return f'{self.userEmail}'
    class Meta:
        verbose_name = "Наш подписчик"
        verbose_name_plural = "Наши подписчики"

class DiscussForUser(models.Model):#+ форма для обсужений - в отдельном блоке - на всех страницах
    #Обсуждение от пользователей Форма готова
    userName = models.CharField(max_length=100, verbose_name='Имя пользователя')
    phoneNumberUser = models.CharField(max_length=50, verbose_name='Номер телефона', validators=[
        ValidateNumberPhone], error_messages={'invalid':'Введите в формате 00x00 или 000x000'})
    emailUser = models.EmailField(max_length=100,unique=True, verbose_name='E-mail пользователя')
    discussContent = models.TextField(max_length=5000, verbose_name='Обсуждение от пользователя')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки')
    userAgree = models.BooleanField(default=False,blank=False, verbose_name='Согласие на ответ')
    def __str__(self):
        return f'{self.userName}'
    class Meta:
        verbose_name = "Обсуждение от подписчика"
        verbose_name_plural = "Обсуждение от подписчиков"

class OurClientsReviews(models.Model):
    # Отзывы наших клиентов
    iconClient = models.ImageField(upload_to="clientReview/photoClient/%Y/%m/%d/", verbose_name='Логотип')
    mainImg = models.ImageField(upload_to="clientReview/mainImg/%Y/%m/%d/", verbose_name='Фотография')
    contentReview = models.TextField(max_length=300, verbose_name='Отзыв')
    nameClient = models.CharField(max_length=50, verbose_name='Имя клиента')
    nameCompany = models.CharField(max_length=100, verbose_name='Название компании')
    adressCompeny = models.CharField(max_length=100, verbose_name='Адрес компании')
    def __str__(self):
        return f'{self.nameCompany}'
    class Meta:
        verbose_name = "Отзыв клиента"
        verbose_name_plural = "Отзывы клиентов"

