from django.db import models

# Create your models here.

#Модели для приложения - aboutUs
class StatisticModel(models.Model):
    #Модель статистика - статические данные
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    valueStatistic = models.CharField(max_length=50, verbose_name='Значение')
    imgUrl = models.ImageField(upload_to="aboutUs/StatisticModel/%Y/%m/%d/", verbose_name='Логотип')
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = "Статистические данные"
        verbose_name_plural = "Статистические данные"


class OurEmployee(models.Model):
    #Модель наши сотрудники
    firstName = models.CharField(max_length=100, verbose_name='Имя')
    secondName = models.CharField(max_length=100, verbose_name='Фамилия')
    jobTitle = models.CharField(max_length=100, verbose_name='Должность')
    imgUrl = models.ImageField(upload_to="aboutUs/OurEmployee/%Y/%m/%d/", verbose_name='Фотография')
    isWork = models.BooleanField(default=True, verbose_name='Действующий сотрудник')
    def __str__(self):
        return f'{self.firstName} {self.secondName}'
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

class OurEmployeeMessage(models.Model):
    #Модель - послание от сотрудника
    title = models.CharField(max_length=150, verbose_name='Оглавление послания')
    message = models.TextField(max_length=10000, verbose_name='Контент послания')
    signature = models.ImageField(upload_to="aboutUs/OurDirectorMessage/%Y/%m/%d/", verbose_name='Подпись')
    employee = models.OneToOneField(OurEmployee, on_delete= models.CASCADE)
    isDisplay = models.BooleanField(default=True, verbose_name='Отобразить')
    time_create = models.DateField(auto_now_add=True, verbose_name='Дата создания') #Время создания объекта класса
    def __str__(self):
        return f'{self.nameDirector}'
    class Meta:
        verbose_name = "Послание от сотрудника"
        verbose_name_plural = "Послание от сотрудников"

class OurHistory(models.Model):
    #Модель наша история - месяц год + к ней слайдер и контент
    dateHistory = models.DateField(verbose_name='Дата истории')
    isPublished = models.BooleanField(default=True, verbose_name='Опубликовать')
    def __str__(self):
        return f'История от {self.dateHistory}'
    class Meta:
        verbose_name = "Наша история"
        verbose_name_plural = "Наши истории"

class OurHistorySlider(models.Model):
    #Модель слайдер к истории - фото + контент
    title = models.CharField(max_length=150, verbose_name='Описание')
    history = models.ForeignKey(OurHistory, on_delete=models.CASCADE, verbose_name='История')
    content = models.TextField(max_length=1000, verbose_name='Контент')
    publishedSlider = models.BooleanField(default=True, verbose_name='Опубликовать')
    historySliderPhoto = models.ImageField(upload_to="aboutUs/OurHistorySlider/%Y/%m/%d/", default=True,verbose_name='Фотография')
    def __str__(self):
        return f'Контент к истории {self.history}'
    class Meta:
        verbose_name = "Слайдер к истории"
        verbose_name_plural = "Слайдеры к истории"

#Модели для приложения - aboutUs - AvaliablePositions
class EmployeeBenefits(models.Model):
    #Модель Выплаты сотрудникам
    titleBenefits = models.CharField(max_length=50, verbose_name='Заголовок')
    contentBenefits = models.TextField(max_length=500, verbose_name='Содержание')
    iconBenefits = models.ImageField(upload_to="aboutUs/EmployeeBenefits/%Y/%m/%d/", verbose_name='Логотип')
    def __str__(self):
        return f'{self.titleBenefits}'
    class Meta:
        verbose_name = "Выплаты сотрудникам"
        verbose_name_plural = "Выплаты сотрудникам"

class OurOfficesModel(models.Model):
    # Модель наши офисы
    listDayWork = [
        ("Monday", "Monday"),("Tuesday", "Tuesday"),("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),("Friday", "Friday"),("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]
    listTimeWork = [
        ("1", "1"),("2", "2"),("3", "3"),("4", "4"),("5", "5"),("6", "6"),("7", "7"),
        ("8", "8"), ("9", "9"), ("10", "10"), ("11", "11"), ("12", "12"), ("13", "13"), ("14", "14"),
        ("15", "15"), ("16", "16"), ("17", "17"), ("18", "18"), ("19", "19"), ("20", "20"), ("21", "21"),
        ("22", "22"), ("23", "23"), ("24", "24"), ("00", "00")
    ]
    nameOffice = models.CharField(max_length=50, verbose_name='Название офиса')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    indexAdress = models.IntegerField(verbose_name='Индекс')
    street = models.CharField(max_length=100, verbose_name='Улица')
    callPhone = models.CharField(max_length=25, verbose_name='Номер телефона офиса')
    emailOffice = models.EmailField(max_length=50, verbose_name='E-mail офиса')
    dayStart = models.CharField(max_length=20,choices=listDayWork, verbose_name='Начало рабочей недели',default="Monday")
    dayStop = models.CharField(max_length=20,choices=listDayWork, verbose_name='Конец рабочей недели',default="Friday")
    timeStart = models.CharField(max_length=20,choices=listTimeWork, verbose_name='Начало рабочего дня', default="00")
    timeStop = models.CharField(max_length=20,choices=listTimeWork, verbose_name='Конец рабочего дня', default="00")
    def __str__(self):
        return f'{self.nameOffice}'
    class Meta:
        verbose_name = "Наш офис"
        verbose_name_plural = "Наши офисы"

class AvaliablePositionsModel(models.Model):
    #Модель вакансии
    operatingTime = [('Full Time','Full Time'),('Part Time','Part Time')]
    title = models.CharField(max_length=100, verbose_name='Название вакансии')
    placeWork = models.ForeignKey(OurOfficesModel,on_delete=models.CASCADE ,verbose_name='Место работы')
    timeWork = models.CharField(max_length=20,choices=operatingTime, default='Full Time',verbose_name='Режим работы')
    published = models.BooleanField(default=True, verbose_name='Опубликовать')
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = "Наша вакансия"
        verbose_name_plural = "Наши вакансии"

class SuscribeUserSVModel(models.Model):
    #Модель подписчик на вакансии + форма для подписки
    userName = models.CharField(max_length=50, verbose_name='Имя подписчика')
    userEmail = models.EmailField(max_length=100, verbose_name='E-mail подписчика')
    dateToSubscribe = models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки')
    isSubscribe = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.userName}'
    class Meta:
        verbose_name = "Подписчик на вакансии"
        verbose_name_plural = "Подписчики на вакансии"

class UserSendCVModel(models.Model):
    #Модель - резюме от пользователей + форма
    userName = models.CharField(max_length=50, verbose_name='Имя соискателя')
    userLocation = models.ForeignKey(OurOfficesModel, on_delete=models.CASCADE ,verbose_name='Место работы соискателя')
    userTell = models.CharField(max_length=20, verbose_name='Телефон соискателя')
    userEmail = models.EmailField(max_length=100, verbose_name='E-mail соискателя')
    userMessage = models.TextField(max_length=2000, verbose_name='Сообщение от соискателя')
    userCVFile = models.FileField(upload_to="aboutUs/UserSendCVModel/%Y/%m/%d/", verbose_name='Файл-резюме')
    dateSend =  models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    def __str__(self):
        return f'{self.userName}'
    class Meta:
        verbose_name = "Соискатель на вакансию"
        verbose_name_plural = "Соискатели на вакансии"

class OurSocLinks(models.Model):
    #Модель - ссылки на соцсети + логотип
    name = models.CharField(max_length=100, verbose_name='Название соц сети')
    nameLink = models.CharField(max_length=100, verbose_name='Имя ссылки')
    link = models.URLField(max_length=1000, verbose_name='Ссылка')
    imgLink_1 = models.ImageField(upload_to="aboutUs/OurSocLinks/%Y/%m/%d/", verbose_name='Логотип соцсети 1')
    imgLink_2 = models.ImageField(upload_to="aboutUs/OurSocLinks/%Y/%m/%d/", verbose_name='Логотип соцсети 2')
    imgLink_2_hover = models.ImageField(upload_to="aboutUs/OurSocLinks/%Y/%m/%d/", verbose_name='Логотип соцсети 2 Hover')
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = "Ссылка в соцсети"
        verbose_name_plural = "Ссылки в соцсетях"