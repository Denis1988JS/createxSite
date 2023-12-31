# Generated by Django 4.2.6 on 2023-10-30 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0002_alter_ourservices_icon_alter_ourservices_icon_hover_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectsOfOurWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Объект работы')),
            ],
            options={
                'verbose_name': 'Объект проекта',
                'verbose_name_plural': 'Объекты проектов',
            },
        ),
        migrations.CreateModel(
            name='OurWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок проекта')),
                ('slug', models.SlugField(max_length=125, unique=True, verbose_name='URL-проекта')),
                ('img', models.ImageField(upload_to='work/%Y/%m/%d/', verbose_name='Главное фото проекта')),
                ('objectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.objectsofourwork', verbose_name='Объект проекта')),
                ('workServicesID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.ourservices', verbose_name='Вид услуги проекта')),
            ],
            options={
                'verbose_name': 'Выполненный проект',
                'verbose_name_plural': 'Выполненные проекты',
            },
        ),
        migrations.CreateModel(
            name='PhotoSliderWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Описание слайдера')),
                ('imgWork', models.ImageField(upload_to='work/WorkSlider/%Y/%m/%d/', verbose_name='Слайдер фото работ')),
                ('workID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.ourwork', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Слайдер-фотографии проекта',
                'verbose_name_plural': 'Слайдер-фотографии проектов',
            },
        ),
        migrations.CreateModel(
            name='OurWorkData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=2500, verbose_name='Описание проекта')),
                ('location', models.CharField(max_length=200, verbose_name='Адрес проекта')),
                ('client', models.CharField(max_length=100, verbose_name='Имя клиента')),
                ('architech', models.CharField(max_length=100, verbose_name='Архитектор')),
                ('size', models.IntegerField(verbose_name='Объем работ')),
                ('price', models.CharField(max_length=20, verbose_name='Стоимость проекта')),
                ('completed', models.DateField()),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.ourwork', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Описание проекта',
                'verbose_name_plural': 'Описание проектов',
            },
        ),
    ]
