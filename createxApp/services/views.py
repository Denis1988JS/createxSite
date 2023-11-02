from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView,View

from createx.models import HeaderContent, OurPartners
from createx.utils import FormsMixin
from services.models import OurServices
from work.models import OurWork


# Create your views here.

#Модель - класс - главная страница services - услуги
class ServicesPage(FormsMixin,ListView):
    model = OurServices
    template_name =  'services/homeservices.html'
    context_object_name = 'services'
    queryset = OurServices.objects.filter(is_active=True)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['title'] = 'Services'
        context['header'] = HeaderContent.objects.get(title='SERVICES')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Модель - класс - страница детально о service - услуга
class ServicesPageDetail(FormsMixin,DetailView):
    model = OurServices
    template_name = 'services/servicesDetail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'service'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['title'] = str(context['service'].title)
        context['header'] = HeaderContent.objects.get(title=str(context['service'].title).upper())
        context['partners'] = OurPartners.objects.all()
        context['sliderForm'] = OurWork.objects.filter(workServicesID__title =context['object'])
        context['slider_name'] ='Related projects'
        print(context['object'])
        context = dict(list(context.items()) + list(c_def.items()))
        return context
