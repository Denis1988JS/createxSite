# Generated by Django 4.2.6 on 2023-10-30 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourservices',
            name='icon',
            field=models.ImageField(upload_to='services/servicesIcon/icon/%Y/%m/%d/', verbose_name='Иконка №1'),
        ),
        migrations.AlterField(
            model_name='ourservices',
            name='icon_hover',
            field=models.ImageField(upload_to='services/servicesIcon/icon_hover/%Y/%m/%d/', verbose_name='Иконка №2 hover'),
        ),
        migrations.AlterField(
            model_name='ourservices',
            name='servicesOfferImg',
            field=models.ImageField(upload_to='services/servicesImg/servicesOfferImg/%Y/%m/%d/', verbose_name='Фотография-offer'),
        ),
    ]
