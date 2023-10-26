from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView,View
from .forms import UserSubscribeForm, DiscussForUserForm

# Create your views here.
#Главная страница сайта
class Homepage(TemplateView):
    template_name = 'createx/homepage.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] ='Createx'
        context['UserSubscribeForm'] = UserSubscribeForm
        context['DiscussForUserForm'] = DiscussForUserForm
        return context

#Обработчик формы
class AddUserSubscribe(View):
    def post(self, request):
        form = UserSubscribeForm(request.POST)
        print(form, request.POST)
        if form.is_valid():
            form = form.save()
            print(form, request.POST)
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