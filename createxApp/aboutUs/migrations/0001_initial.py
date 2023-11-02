# Generated by Django 4.2.6 on 2023-11-02 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeBenefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleBenefits', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('contentBenefits', models.TextField(max_length=500, verbose_name='Содержание')),
                ('iconBenefits', models.ImageField(upload_to='aboutUs/EmployeeBenefits/%Y/%m/%d/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Выплаты сотрудникам',
                'verbose_name_plural': 'Выплаты сотрудникам',
            },
        ),
        migrations.CreateModel(
            name='OurEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100, verbose_name='Имя')),
                ('secondName', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('jobTitle', models.CharField(max_length=100, verbose_name='Должность')),
                ('imgUrl', models.ImageField(upload_to='aboutUs/OurEmployee/%Y/%m/%d/', verbose_name='Фотография')),
                ('isWork', models.BooleanField(default=True, verbose_name='Действующий сотрудник')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='OurHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateHistory', models.DateField(verbose_name='Дата истории')),
                ('isPublished', models.BooleanField(default=True, verbose_name='Опубликовать')),
            ],
            options={
                'verbose_name': 'Наша история',
                'verbose_name_plural': 'Наши истории',
            },
        ),
        migrations.CreateModel(
            name='OurOfficesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOffice', models.CharField(max_length=50, verbose_name='Название офиса')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('indexAdress', models.IntegerField(verbose_name='Индекс')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('callPhone', models.CharField(max_length=25, verbose_name='Номер телефона офиса')),
                ('emailOffice', models.EmailField(max_length=50, verbose_name='E-mail офиса')),
                ('dayStart', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=20, verbose_name='Начало рабочей недели')),
                ('dayStop', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Friday', max_length=20, verbose_name='Конец рабочей недели')),
                ('timeStart', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('00', '00')], default='00', max_length=20, verbose_name='Начало рабочего дня')),
                ('timeStop', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('00', '00')], default='00', max_length=20, verbose_name='Конец рабочего дня')),
            ],
            options={
                'verbose_name': 'Наш офис',
                'verbose_name_plural': 'Наши офисы',
            },
        ),
        migrations.CreateModel(
            name='OurSocLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название соц сети')),
                ('nameLink', models.CharField(max_length=100, verbose_name='Имя ссылки')),
                ('link', models.URLField(max_length=1000, verbose_name='Ссылка')),
                ('imgLink_1', models.ImageField(upload_to='aboutUs/OurSocLinks/%Y/%m/%d/', verbose_name='Логотип соцсети 1')),
                ('imgLink_2', models.ImageField(upload_to='aboutUs/OurSocLinks/%Y/%m/%d/', verbose_name='Логотип соцсети 2')),
                ('imgLink_2_hover', models.ImageField(upload_to='aboutUs/OurSocLinks/%Y/%m/%d/', verbose_name='Логотип соцсети 2 Hover')),
            ],
            options={
                'verbose_name': 'Ссылка в соцсети',
                'verbose_name_plural': 'Ссылки в соцсетях',
            },
        ),
        migrations.CreateModel(
            name='StatisticModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('valueStatistic', models.CharField(max_length=50, verbose_name='Значение')),
                ('imgUrl', models.ImageField(upload_to='aboutUs/StatisticModel/%Y/%m/%d/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Статистические данные',
                'verbose_name_plural': 'Статистические данные',
            },
        ),
        migrations.CreateModel(
            name='SuscribeUserSVModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50, verbose_name='Имя подписчика')),
                ('userEmail', models.EmailField(max_length=100, verbose_name='E-mail подписчика')),
                ('dateToSubscribe', models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки')),
                ('isSubscribe', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Подписчик на вакансии',
                'verbose_name_plural': 'Подписчики на вакансии',
            },
        ),
        migrations.CreateModel(
            name='UserSendCVModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50, verbose_name='Имя соискателя')),
                ('userTell', models.CharField(max_length=20, verbose_name='Телефон соискателя')),
                ('userEmail', models.EmailField(max_length=100, verbose_name='E-mail соискателя')),
                ('userMessage', models.TextField(max_length=2000, verbose_name='Сообщение от соискателя')),
                ('userCVFile', models.FileField(upload_to='aboutUs/UserSendCVModel/%Y/%m/%d/', verbose_name='Файл-резюме')),
                ('dateSend', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
                ('userLocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutUs.ourofficesmodel', verbose_name='Место работы соискателя')),
            ],
            options={
                'verbose_name': 'Соискатель на вакансию',
                'verbose_name_plural': 'Соискатели на вакансии',
            },
        ),
        migrations.CreateModel(
            name='OurHistorySlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Описание')),
                ('content', models.TextField(max_length=1000, verbose_name='Контент')),
                ('publishedSlider', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('historySliderPhoto', models.ImageField(default=True, upload_to='aboutUs/OurHistorySlider/%Y/%m/%d/', verbose_name='Фотография')),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutUs.ourhistory', verbose_name='История')),
            ],
            options={
                'verbose_name': 'Слайдер к истории',
                'verbose_name_plural': 'Слайдеры к истории',
            },
        ),
        migrations.CreateModel(
            name='OurEmployeeMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Оглавление послания')),
                ('message', models.TextField(max_length=10000, verbose_name='Контент послания')),
                ('signature', models.ImageField(upload_to='aboutUs/OurDirectorMessage/%Y/%m/%d/', verbose_name='Подпись')),
                ('isDisplay', models.BooleanField(default=True, verbose_name='Отобразить')),
                ('time_create', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aboutUs.ouremployee')),
            ],
            options={
                'verbose_name': 'Послание от сотрудника',
                'verbose_name_plural': 'Послание от сотрудников',
            },
        ),
        migrations.CreateModel(
            name='AvaliablePositionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название вакансии')),
                ('timeWork', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default='Full Time', max_length=20, verbose_name='Режим работы')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('placeWork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutUs.ourofficesmodel', verbose_name='Место работы')),
            ],
            options={
                'verbose_name': 'Наша вакансия',
                'verbose_name_plural': 'Наши вакансии',
            },
        ),
    ]