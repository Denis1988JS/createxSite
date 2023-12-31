# Generated by Django 4.2.6 on 2023-10-27 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurBenefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Преимущество')),
                ('content', models.TextField(verbose_name='Контент')),
                ('icon', models.ImageField(upload_to='services/benefits/%Y/%m/%d/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Наше преимущество',
                'verbose_name_plural': 'Наши преимущества',
            },
        ),
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1250, verbose_name='Наименование услуги')),
                ('content', models.TextField(verbose_name='Описание услуги')),
                ('slug', models.SlugField(max_length=125, unique=True, verbose_name='URL-услуги')),
                ('servicesImg', models.ImageField(upload_to='services/servicesImg/Logo/%Y/%m/%d/', verbose_name='Логотип')),
                ('servicesOfferImg', models.ImageField(upload_to='services/servicesImg/servicesOfferImg/%Y/%m/%d/', verbose_name='Фотография')),
                ('icon', models.ImageField(upload_to='services/servicesIcon/icon/%Y/%m/%d/', verbose_name='Картинка №1')),
                ('icon_hover', models.ImageField(upload_to='services/servicesIcon/icon_hover/%Y/%m/%d/', verbose_name='Картинка №2 hover')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Наша услуга',
                'verbose_name_plural': 'Наши услуги',
            },
        ),
        migrations.CreateModel(
            name='ourOfferServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleOffer', models.CharField(max_length=100, verbose_name='Заголовок сервиса')),
                ('contentOffer', models.TextField(max_length=1000, verbose_name='Описание сервиса')),
                ('servicesID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.ourservices', verbose_name='Наименование услуги')),
            ],
            options={
                'verbose_name': 'Наша оферта',
                'verbose_name_plural': 'Наша оферта',
            },
        ),
    ]
