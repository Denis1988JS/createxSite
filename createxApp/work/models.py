from django.db import models
from django.urls import reverse_lazy

from services.models import OurServices


# Create your models here.
#Модель адрес(объект) проекта
class ObjectsOfOurWork(models.Model):
    name = models.CharField(max_length=150, verbose_name='Объект работы')
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = "Объект проекта"
        verbose_name_plural = "Объекты проектов"

#Модель - работа(услуга) - work
class OurWork(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок проекта')
    slug = models.SlugField(max_length=125,unique=True, db_index=True, verbose_name='URL-проекта' )
    objectID = models.ForeignKey(ObjectsOfOurWork, on_delete=models.CASCADE, verbose_name='Объект проекта')
    img = models.ImageField(upload_to='work/%Y/%m/%d/', verbose_name='Главное фото проекта')
    workServicesID = models.ForeignKey(OurServices,on_delete=models.CASCADE, verbose_name='Вид услуги проекта')
    def __str__(self):
        return f'{self.title}'
    def get_absolute_url(self):#Ссылка на url по слагу
        return reverse_lazy('work', kwargs={'slug':self.slug})
    class Meta:
        verbose_name = "Выполненный проект"
        verbose_name_plural = "Выполненные проекты"

#Модель - фотографии для выполненного проекта - слайдер
class PhotoSliderWork(models.Model):
    title = models.CharField(max_length=150, verbose_name='Описание слайдера')
    imgWork = models.ImageField(upload_to='work/WorkSlider/%Y/%m/%d/', verbose_name='Слайдер фото работ')
    workID = models.ForeignKey(OurWork, on_delete=models.CASCADE, verbose_name='Проект')
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = "Слайдер-фотографии проекта"
        verbose_name_plural = "Слайдер-фотографии проектов"

#Модель - описание работы
class OurWorkData(models.Model):
    content = models.TextField(max_length=2500, verbose_name='Описание проекта')
    location = models.CharField(max_length=200, verbose_name='Адрес проекта')
    client = models.CharField(max_length=100, verbose_name='Имя клиента')
    architech = models.CharField(max_length=100, verbose_name='Архитектор')
    size = models.IntegerField(verbose_name='Объем работ')
    price = models.CharField(max_length=20, verbose_name='Стоимость проекта')
    completed = models.DateField()
    work = models.ForeignKey(OurWork, on_delete=models.CASCADE, verbose_name='Проект')
    def __str__(self):
        return f'{self.location} {self.work}'
    class Meta:
        verbose_name = "Описание проекта"
        verbose_name_plural = "Описание проектов"