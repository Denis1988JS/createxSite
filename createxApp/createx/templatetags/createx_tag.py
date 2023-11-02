from django import template
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

