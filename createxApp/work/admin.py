from django.contrib import admin
from django.utils.safestring import mark_safe

from work.models import ObjectsOfOurWork, OurWork, PhotoSliderWork, OurWorkData


# Register your models here.


#Админка - адрес(объект) проекта
class OurWorkInLine(admin.TabularInline):
    model = OurWork
    classes = ('collapse',)
    extra = 1
class ObjectsOfOurWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    inlines = (OurWorkInLine,)
    ordering = ['id']
admin.site.register(ObjectsOfOurWork,ObjectsOfOurWorkAdmin)

#Модель - работа(услуга) - work + инлайны для модели
class PhotoSliderWorkInLine(admin.TabularInline):
    model = PhotoSliderWork
    classes = ('collapse',)
    extra = 1

class OurWorkDataInLine(admin.TabularInline):
    model = OurWorkData
    classes = ('collapse',)
    extra = 1

class OurWorkAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','objectID','workServicesID','getImg')
    list_display_links =('id','title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'workServicesID')
    search_help_text = ('Поиск по проектам')
    list_filter = ('workServicesID', 'objectID')
    inlines = (PhotoSliderWorkInLine, OurWorkDataInLine)
    readonly_fields =('getImg',)
    fieldsets = (
        (None, {
              "fields": (("title", "slug",),)#В одну строку
        }),
        (None, {
            "fields": (("objectID", "workServicesID",),)  # В одну строку
        }),
        (None, {
            "fields": (("img", "getImg",),)  # В одну строку
        }),
    )
    def getImg(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=100>")
    getImg.short_description = 'Главное фото'
admin.site.register(OurWork,OurWorkAdmin)

#Модель - Слайдер проекта - PhotoSliderWork
class PhotoSliderWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','getImgWork','workID')
    list_display_links = ('id', 'title','getImgWork')
    list_filter = ('workID',)
    ordering = ['workID']
    def getImgWork(self, object):
        if object.imgWork:
            return mark_safe(f"<img src='{object.imgWork.url}' width=35>")
    getImgWork.short_description = 'Фото слайдера'
admin.site.register(PhotoSliderWork,PhotoSliderWorkAdmin)

class OurWorkDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'work','location','client','architech','price')
    list_display_links = ('id', 'work','location','client','architech','price')
admin.site.register(OurWorkData,OurWorkDataAdmin)