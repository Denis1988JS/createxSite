from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView,View
import datetime
from datetime import date, datetime

from createx.models import HeaderContent
from createx.utils import FormsMixin
from news.forms import NewsCommentsModeflForm
from news.models import NewsModel, CategoryNews, NewsCommentsModefl
import json

#Функции для AJAX
#Кол-во комментариев
def countComments(data):
    for item in data:
        comment = NewsCommentsModefl.objects.filter(news__id=item["id"])
        counter = comment.count()
        if counter >0:
            item["counter"] = f'{counter} comments'
        else:
            item["counter"] = 'No comments'

#Срез 150 для content
def sliceContent(data):  # Получение строки - объект работы!!!
    for item in data:
        for values in item:
            if values == 'content':
                item[values] = item[values][0:150]
#Обработка даты в json
def myconverter(o):
    if isinstance(o, (datetime, date)):
        o = o.strftime('%B %d , %Y')
        o= o.__str__()
        return o
#Получаем строку категория новости
def takeCategoryNews(data):  # Получение строки - объект работы!!!
    for item in data:
        item['cat_id'] = item['categoryID']
        for values in item:
            if values == 'categoryID':
                cat = CategoryNews.objects.get(id=item[values])
                item[values] = cat.__str__()
#Получаем все категории новостей
class CategoryAll:
    def getCategory(self):
        return CategoryNews.objects.all()
#Страница новости

class NewsPage(CategoryAll,FormsMixin,ListView):
    model =  NewsModel
    template_name = 'news/newspage.html'
    context_object_name = 'news'
    paginate_by = 4
    queryset = NewsModel.objects.filter(is_published=True).select_related('categoryID')

    def post(self, request, *args, **kwargs):
        rb = eval(request.body.decode())
        if request.method == 'POST' and rb['categoryID']!='All':
            data = json.loads(request.body)
            queryset = NewsModel.objects.filter(categoryID__id=data['categoryID'],is_published=True).distinct().values('id', 'title', 'img',
                                                                                                            'categoryID', 'slug', 'content',
                                                                                                            'date_publish')
            takeCategoryNews(queryset)
            sliceContent(queryset)
            countComments(queryset)
            queryset = list(queryset)
            queryset = json.dumps(queryset,  default = myconverter)
            queryset = JsonResponse(queryset, safe=False)
            return queryset
        elif request.method == 'POST' and rb['categoryID']=='All':
            data = json.loads(request.body)
            queryset = NewsModel.objects.filter(is_published=True).distinct().values('id', 'title', 'img',
                                                                                                                        'categoryID', 'slug',
                                                                                                                        'content',
                                                                                                                        'date_publish')
            takeCategoryNews(queryset)
            sliceContent(queryset)
            countComments(queryset)
            queryset = list(queryset)
            queryset = json.dumps(queryset, default=myconverter)
            queryset = JsonResponse(queryset, safe=False)
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['title'] = 'News'
        context['header'] = HeaderContent.objects.get(title='NEWS')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


#Детально - про новость
class NewsDetail(FormsMixin,DetailView):
    model = NewsModel
    template_name = 'news/newsDetailPage.html'
    context_object_name = 'news'
    slug_url_kwarg = 'slug'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['title'] = context['object']
        context['form'] = NewsCommentsModeflForm
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Добавление комментария
class AddComment(View):

    def post(self, request, pk):
        form = NewsCommentsModeflForm(request.POST)
        news = NewsModel.objects.get(id=pk)
        if form.is_valid():
            comment = NewsCommentsModefl()
            comment.user_name = self.request.POST.get('user_name')
            comment.user_email = self.request.POST.get('user_email')
            comment.comment = self.request.POST.get('comment')
            comment.news = NewsModel.objects.get(id=self.request.POST.get('news'))
            comment.date_publish = datetime.now()
            comment.is_published = True
            print(request.POST)
            if request.POST.get("parent"):
                comment.parent_id = int(request.POST.get("parent"))
                print(comment.parent_id)
                comment.save()
            comment.save()
        return redirect(news.get_absolute_url())