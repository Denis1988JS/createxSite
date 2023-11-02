from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class OurServices(models.Model):
    # Модель наши сервисы(услуги) - OurServices
    title = models.CharField(max_length=1250, verbose_name='Наименование услуги')
    content = models.TextField(verbose_name='Описание услуги')
    slug = models.SlugField(max_length=125,unique=True, db_index=True, verbose_name='URL-услуги')
    servicesImg = models.ImageField(upload_to='services/servicesImg/Logo/%Y/%m/%d/', verbose_name='Логотип')
    servicesOfferImg = models.ImageField(upload_to='services/servicesImg/servicesOfferImg/%Y/%m/%d/', verbose_name='Фотография-offer')
    icon = models.ImageField(upload_to='services/servicesIcon/icon/%Y/%m/%d/', verbose_name='Иконка №1')
    icon_hover = models.ImageField(upload_to='services/servicesIcon/icon_hover/%Y/%m/%d/', verbose_name='Иконка №2 hover')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.title}'
    def get_absolute_url(self):#Ссылка на url по слагу
        return reverse_lazy('services', kwargs={'slug':self.slug})
    class Meta:
        verbose_name = "Наша услуга"
        verbose_name_plural = "Наши услуги"


class ourOfferServices(models.Model):
    # Модель оферта к сервису(услуги) - ourOfferServices
    titleOffer = models.CharField(max_length=100, verbose_name='Заголовок сервиса')
    contentOffer = models.TextField(max_length=1000, verbose_name='Описание сервиса')
    servicesID = models.ForeignKey(OurServices, on_delete=models.CASCADE, verbose_name='Наименование услуги')
    def __str__(self):
        return f'{self.titleOffer}'
    class Meta:
        verbose_name = "Наша оферта"
        verbose_name_plural = "Наша оферта"


class OurBenefits(models.Model):
    # Модель наши преимущества - Our benefits
    title = models.CharField(max_length=100, verbose_name='Преимущество')
    content = models.TextField(verbose_name='Контент')
    icon = models.ImageField(upload_to='services/benefits/%Y/%m/%d/', verbose_name='Логотип')
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = "Наше преимущество"
        verbose_name_plural = "Наши преимущества"