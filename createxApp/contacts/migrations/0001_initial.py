# Generated by Django 4.2.6 on 2023-11-14 15:06

import contacts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0002_alter_ourservices_icon_alter_ourservices_icon_hover_and_more'),
        ('aboutUs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phoneNumberUser', models.CharField(error_messages={'invalid': 'Введите в формате 00x00 или 000x000'}, max_length=50, validators=[contacts.models.ValidateNumberPhone], verbose_name='Номер телефона')),
                ('userEmail', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('contact', models.CharField(choices=[('Phone', 'Phone'), ('Email', 'Email'), ('Viber', 'Viber'), ('Whatsapp', 'Whatsapp')], max_length=50, verbose_name='Тип связи')),
                ('userMessage', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('userAgree', models.BooleanField(default=False, verbose_name='Согласие на ответ')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата вопроса')),
                ('interesting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.ourservices', verbose_name='Услуга')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutUs.ourofficesmodel', verbose_name='Офис')),
            ],
            options={
                'verbose_name': 'Сообщение от пользователя',
                'verbose_name_plural': 'Сообщения от пользователей',
            },
        ),
    ]
