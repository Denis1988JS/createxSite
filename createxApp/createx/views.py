from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView,View

from services.models import OurServices
from work.models import OurWork
from .forms import UserSubscribeForm, DiscussForUserForm,AskFromUserForm
from .models import OurPartners
from  .utils import FormsMixin

# Create your views here.
#Главная страница сайта
class Homepage(FormsMixin, TemplateView):
    template_name = 'createx/homepage.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['title'] ='Createx'
        context['UserSubscribeForm'] = UserSubscribeForm
        context['DiscussForUserForm'] = DiscussForUserForm
        context['AskFromUserForm'] = AskFromUserForm
        context['services'] = OurServices.objects.filter(is_active=True)
        context['partners'] = OurPartners.objects.all()
        context['sliderForm'] = OurWork.objects.all().reverse()[1:7]
        context['slider_name'] = 'Browse our selected projects and learn more about our work'
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Обработчик формы
class AddUserSubscribe(View):
    def post(self, request):
        form = UserSubscribeForm(request.POST)
        if form.is_valid():
            form = form.save()
        else:
            print('Ошибка')
        return redirect('home')

#Обработчик формы добавления DiscussForUserForm - DiscussForUser
def addDiscussForUser(request):
    if request.method == 'POST':
        form = DiscussForUserForm(request.POST)
        if form.is_valid():
            form = form.save()
        else:
            print('Ошибка',form)
        return redirect('home')
#Обработчик формы добавления вопроса AskFromUserForm - AskFromUser
class AddAsk(View):
    def post(self, request):
        form = AskFromUserForm(request.POST)
        if form.is_valid():
            form = form.save()
        else:
            print('Ошибка')
        return redirect('home')