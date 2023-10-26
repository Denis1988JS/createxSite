from django import template
from createx.models import MainSliderModel


register = template.Library()


#Передаем шаблон через inclusion_tag
@register.inclusion_tag('createx/tags/mainSliderBlock.html')
def get_main_slider():
    slider = MainSliderModel.objects.all()
    return {"slider": slider}
