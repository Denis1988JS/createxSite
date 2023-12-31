import turtle

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView,View

from createx.models import HeaderContent
from createx.utils import FormsMixin
from services.models import OurServices
from work.models import OurWork, ObjectsOfOurWork, PhotoSliderWork
import json
from django.http import JsonResponse

# Create your views here.
def takeObjects(data):  # Получение строки - объект работы!!!
    for item in data:
        for values in item:
            if values == 'objectID':
                fP = ObjectsOfOurWork.objects.get(id=item[values])
                item[values] = fP.__str__()

class WorkPage(FormsMixin,ListView):
    model = OurWork
    template_name = 'work/workPage.html'
    context_object_name = 'work'
    queryset = OurWork.objects.all()
    def post(self, request):
        rb = eval(request.body.decode())
        if request.method == 'POST' and rb['workServicesID'] != 'All':
                data = json.loads(request.body)
                newWorks = OurWork.objects.filter(workServicesID__title=data['workServicesID']).values('id','title','slug','objectID', 'img','workServicesID')[0:6]
                takeObjects(newWorks)
                newWorks = list(newWorks)
                newWorks = json.dumps(newWorks)
                return JsonResponse(newWorks, safe=False)
        elif  request.method == 'POST' and rb['workServicesID'] == 'All':
                newWorks = OurWork.objects.all().values('id','title','slug','objectID', 'img','workServicesID')[0:6]
                takeObjects(newWorks)
                newWorks = list(newWorks)
                newWorks = json.dumps(newWorks)
                return JsonResponse(newWorks, safe=False)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['title'] = 'Work'
        context['header'] = HeaderContent.objects.get(title='OUR WORK')
        context['services'] = OurServices.objects.filter(is_active=True)
        context['works'] = OurWork.objects.all().select_related('objectID')[0:6]
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Детально - про выполненную работу
class WorkDetail(FormsMixin,DetailView):
    model = OurWork
    template_name = 'work/workDetailPage.html'
    context_object_name = 'work'
    slug_url_kwarg = 'slug'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['title'] = context['object']
        context['first_slide'] = context['object'].photoSlider.first()
        context['sliderForm'] = OurWork.objects.filter(objectID__name = context['object'].objectID)
        context['slider_name'] = 'Similar projects'
        context = dict(list(context.items()) + list(c_def.items()))
        return context