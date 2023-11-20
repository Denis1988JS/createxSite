from django.db import models
from django.urls import reverse_lazy, reverse


# Create your models here.


class CategoryNews(models.Model):
    #Категория новостей
    name = models.CharField(max_length=50, verbose_name='Название категории')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL-категории')
    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):#Ссылка на url по слагу
        return reverse_lazy('news/category/', kwargs={'slug':self.slug})
    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"

class NewsModel(models.Model):
    #Модель новости
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    img = models.ImageField(upload_to='news/%Y/%m/%d/', verbose_name='Главное фото')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL-новости')
    content = models.TextField(verbose_name='Контент')
    date_publish = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    categoryID = models.ForeignKey(CategoryNews,on_delete=models.CASCADE, verbose_name='Тема новости')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    def __str__(self):
        return f'{self.title} {self.date_publish}'

    def get_absolute_url(self):#Ссылка на url по слагу
        return reverse('newsDetail', kwargs={'slug':self.slug})
    def get_comment_count(self):
        len = self.newscommentsmodefl_set.filter(news__id=self.pk)
        counter = len.count()

        return counter
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class NewsCommentsModefl(models.Model):
    #Комментарии к новости
    user_name = models.CharField(max_length=50, verbose_name='Комментатор')
    user_email = models.EmailField(max_length=100, verbose_name='e-mail комментатора')
    comment = models.TextField(max_length=5000, verbose_name='Комментарий')
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE, verbose_name='Новость')
    date_publish = models.DateField(auto_now_add=True, verbose_name='Дата комментария')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return f'{self.user_name} {self.user_email} {self.news}'
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
