from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView,View
from django.shortcuts import render, redirect
from  django.contrib import messages
from aboutUs.forms import SuscribeUserSVModelForm, UserSendCVModelForm
from aboutUs.models import StatisticModel, OurEmployeeMessage, OurHistory, OurHistorySlider, OurEmployee, AvaliablePositionsModel, \
    EmployeeBenefits
from createx.models import HeaderContent, OurPartners
from createx.utils import FormsMixin
import json
from django.http import JsonResponse

# Create your views here.
#Страница about us - о нас
class AboutUsHomepage(FormsMixin, TemplateView):
    template_name = 'aboutUs/aboutUshomepage.html'
    def post(self, request):
        if request.method == "POST":
            data = json.loads(request.body)
            newHistorySlider = OurHistorySlider.objects.filter(history__id=data['id'], publishedSlider=True).values('id','title','content','history', \
                               'historySliderPhoto')
            newHistorySlider = list(newHistorySlider)
            newHistorySlider = json.dumps(newHistorySlider)
            return JsonResponse(newHistorySlider, safe=False)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['header'] = HeaderContent.objects.get(title='ABOUT US')
        context['statistics'] = StatisticModel.objects.all()
        context['messages'] = OurEmployeeMessage.objects.all()
        context['histories'] = OurHistory.objects.filter(isPublished=True)[0:9]
        context['sliders'] = OurHistorySlider.objects.filter(history__id=1)
        context['partners'] = OurPartners.objects.all()
        context['teams'] = OurEmployee.objects.filter(isWork=True)
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return  context

#Страница avaliablePositions - доступные вакансии

class AvaliablePositions(FormsMixin, ListView):
    model = AvaliablePositionsModel
    template_name = 'aboutUs/AvaliablePositions.html'
    context_object_name = 'avaliables'
    queryset = AvaliablePositionsModel.objects.filter(published=True)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Avaliable Positions'
        context['header'] = HeaderContent.objects.get(title='AVAILABLE POSITIONS')
        context['SuscribeUserSVModelForm'] = SuscribeUserSVModelForm
        context['UserSendCVModelForm'] = UserSendCVModelForm
        context['benefits'] = EmployeeBenefits.objects.all()
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Страница SuscribeUserSVModelForm - подписка на вакансии

class SuscribeUserSVModelAdd(View):
    def post(self, request):
        form = SuscribeUserSVModelForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Вы успешно подписались на вакансии')
            return redirect('avaliablePositions')
        else:
            messages.success(request, 'Подписаться на вакансии не удалось')
            return redirect('avaliablePositions')

#Страница UserSendCVModelForm - отправка резюме

class UserSendCVModelAdd(View):
    def post(self, request):
        form = UserSendCVModelForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Резюме отправлено !!!')
            return redirect('avaliablePositions')
        else:
            messages.success(request, 'Отправить резюме не удалось !')
            return redirect('avaliablePositions')


