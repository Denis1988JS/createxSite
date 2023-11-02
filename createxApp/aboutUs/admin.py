from django.contrib import admin
from django.utils.safestring import mark_safe

from aboutUs.models import StatisticModel, OurEmployee, EmployeeBenefits, OurOfficesModel, AvaliablePositionsModel


# Register your models here.
#Админка - статистические данные - StatisticModel
class StatisticModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','valueStatistic','getimgUrl')
    list_display_links = ('id', 'title')
    list_editable = ('valueStatistic',)
    readonly_fields = ("getimgUrl",)
    fieldsets = (
        (None, {
            "fields": (("title", "valueStatistic"),)  # В одну строку
        }),
        (None, {
            "fields": (("imgUrl", "getimgUrl"),)  # В одну строку
        }),
    )
    def getimgUrl(self, object):
        if object.imgUrl:
            return mark_safe(f"<img src='{object.imgUrl.url}' width=50>")
    getimgUrl.short_description = 'Фото'
admin.site.register(StatisticModel,StatisticModelAdmin)

#Админка наши сотрудники - OurEmployee
class OurEmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'getFullName', 'jobTitle', 'getimgUrl','isWork',)
    list_display_links = ('id', 'getFullName',)
    list_editable = ('isWork',)
    readonly_fields = ("getimgUrl",)
    ordering = ['pk']
    fieldsets = (
        (None, {
            "fields": ('jobTitle',("firstName", "secondName",'isWork'))  # В одну строку
        }),
        (None, {
            "fields": (("imgUrl", "getimgUrl"),)  # В одну строку
        }),
    )
    def getimgUrl(self, object):
        if object.imgUrl:
            return mark_safe(f"<img src='{object.imgUrl.url}' width=150>")
    getimgUrl.short_description = 'Фото'
    def getFullName(self,object):
        fullName = f'{object.firstName} {object.secondName}'
        return  fullName
    getFullName.short_description = 'ФИО'
admin.site.register(OurEmployee, OurEmployeeAdmin)

#Админка - EmployeeBenefits - преимищество сотрудников (Выплаты сотрудникам)
class EmployeeBenefitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'titleBenefits','getBenefitsIcon')
    list_display_links = ('id', 'titleBenefits')
    readonly_fields = ("getBenefitsIcon",)

    def getBenefitsIcon(self, object):
        if object.iconBenefits:
            return mark_safe(f"<img src='{object.iconBenefits.url}' width=100>")
    getBenefitsIcon.short_description = 'Фото'
admin.site.register(EmployeeBenefits, EmployeeBenefitsAdmin)


#Админка - OurIfficesModel - наши офисы - опечатка в названии модели
class OurOfficesModelAdmin(admin.ModelAdmin):
    list_display = ('id','nameOffice','getFullADress','callPhone','emailOffice','getDayWork','getTimeWork' )
    list_display_links = ('id','nameOffice', 'getFullADress')
    list_editable = ('callPhone','emailOffice')
    readonly_fields = ("getFullADress",'getTimeWork','getDayWork')
    fieldsets = (
        (None, {
            "fields": ('getFullADress',("nameOffice", "country",'city','indexAdress','street'))  # В одну строку
        }),
        (None, {
            "fields": (("callPhone", "emailOffice",),)  # В одну строку
        }),
        (None, {
            "fields": ("getDayWork",("dayStart", "dayStop",))  # В одну строку
        }),
        (None, {
            "fields": ( "getTimeWork",("timeStart", "timeStop",))  # В одну строку
        }),
    )
    def getFullADress(self,object):
        fullADress = f'{object.indexAdress}-{object.country}-{object.city}-{object.street}'
        return  fullADress
    getFullADress.short_description = 'Данные офиса'
    def getDayWork(self, object):
        dayWork = f'{object.dayStart}-{object.dayStop}'
        return dayWork
    getDayWork.short_description = 'Дни работы'
    def getTimeWork(self, object):
        timeWork = f'{object.timeStart}-{object.timeStop}'
        return timeWork
    getTimeWork.short_description = 'Режим работы'
admin.site.register(OurOfficesModel, OurOfficesModelAdmin)

#Админка - AvaliablePositionsModel - модель вакансия
class AvaliablePositionsModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','placeWork','timeWork','published')
    list_display_links = ('id','title')
    list_editable = ('published',)
    fieldsets = (
        (None, {
            "fields": ('title',("placeWork", "timeWork"))  # В одну строку
        }),
        (None, {
            "fields": (("published",),)  # В одну строку
        }),
    )
admin.site.register(AvaliablePositionsModel, AvaliablePositionsModelAdmin)