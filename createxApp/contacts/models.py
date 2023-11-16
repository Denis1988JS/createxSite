import re
from django.core.exceptions import ValidationError
from django.db import models

from aboutUs.models import OurOfficesModel
from services.models import OurServices

def ValidateNumberPhone(size):
    pattern = r"^\+?[123456789][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$"
    p = re.compile(pattern)
    rezult = p.search(size)
    if not rezult:
        raise ValidationError('Номер телефона в формате 81234567890 или +71234567890')

# Create your models here.
class Contacts(models.Model):
    contact_method = [
        ("Phone","Phone"),
        ("Email","Email"),
        ("Viber","Viber"),
        ("Whatsapp", "Whatsapp"),
    ]
    name = models.CharField(max_length=100, verbose_name='Имя')
    interesting = models.ForeignKey(OurServices, on_delete=models.CASCADE, verbose_name='Услуга' )
    phoneNumberUser = models.CharField(max_length=50, verbose_name='Номер телефона', validators=[
        ValidateNumberPhone], error_messages={'invalid': 'Введите в формате 00x00 или 000x000'})
    location = models.ForeignKey(OurOfficesModel,on_delete=models.CASCADE ,verbose_name='Офис')
    userEmail = models.EmailField(max_length=100, verbose_name='E-mail')
    contact =  models.CharField(max_length=50, choices=contact_method,verbose_name='Тип связи')
    userMessage = models.TextField(max_length=5000, verbose_name='Сообщение')
    userAgree = models.BooleanField(default=False, blank=False, verbose_name='Согласие на ответ')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата вопроса')

    def __str__(self):
        return f'{self.name} {self.userEmail} {self.date}'
    class Meta:
        verbose_name = "Сообщение от пользователя"
        verbose_name_plural = "Сообщения от пользователей"
