from django import template

from aboutUs.models import OurOfficesModel, OurSocLinks
from createx.models import MainSliderModel, OurCoreValues, OurClientsReviews
from services.models import OurBenefits

register = template.Library()


#Передаем шаблон через inclusion_tag - модель главный слайдер
@register.inclusion_tag('createx/tags/mainSliderBlock.html')
def get_main_slider():
    slider = MainSliderModel.objects.all()
    return {"slider": slider}


#Передаем шаблон через inclusion_tag - модель OurCoreValues
@register.inclusion_tag('createx/tags/OurCoreValues.html')
def getOurCoreValues():
    ocv = OurCoreValues.objects.all()
    return {"ocv": ocv}


#Передаем шаблон через inclusion_tag - модель OurClientsReviews
@register.inclusion_tag('createx/tags/OurClientsReviews.html')
def getOurClientsReviews():
    sliders = OurClientsReviews.objects.all()
    return {"sliders": sliders}


#Передаем шаблон через inclusion_tag - модель OurBenefits
@register.inclusion_tag('createx/tags/OurBenefits.html')
def getOurBenefits():
    benefits = OurBenefits.objects.all()
    return {"benefits": benefits}

#Передаем шаблон через inclusion_tag - модель OurOfficesModel
@register.inclusion_tag('createx/tags/OurOffices.html')
def OurOffices():
    offices = OurOfficesModel.objects.all()
    return {"offices": offices}

#Передаем шаблон - модель на все соц сети
@register.simple_tag()
def get_soc_links():
    return OurSocLinks.objects.all()
