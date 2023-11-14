from django.contrib import admin
from django.utils.safestring import mark_safe

from aboutUs.models import StatisticModel, OurEmployee, EmployeeBenefits, OurOfficesModel, AvaliablePositionsModel, SuscribeUserSVModel, \
    UserSendCVModel, OurSocLinks, OurEmployeeMessage, OurHistory, OurHistorySlider


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
class OurEmployeeMessageInline(admin.TabularInline):
    model = OurEmployeeMessage
    classes = ('collapse',)
    readonly_fields = ('getSignature',)
    extra = 1
    def getSignature(self, object):
        if object.signature:
            return mark_safe(f"<img src='{object.signature.url}' width=100>")
    getSignature.short_description = 'Подпись'
class OurEmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'getFullName', 'jobTitle', 'getimgUrl','isWork',)
    list_display_links = ('id', 'getFullName',)
    list_editable = ('isWork',)
    readonly_fields = ("getimgUrl",)
    inlines = [OurEmployeeMessageInline]
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

#Админка - OurEmployeeMessage - послание от сотрудника
class OurEmployeeMessageAdmin(admin.ModelAdmin):
    list_display = ('id','title','employee','isDisplay','time_create','getSignature')
    list_display_links = ('id','title',)
    list_editable = ('isDisplay',)
    list_filter = ('employee',)
    readonly_fields = ('getSignature',)
    def getSignature(self, object):
        if object.signature:
            return mark_safe(f"<img src='{object.signature.url}' width=100>")
    getSignature.short_description = 'Подпись'
admin.site.register(OurEmployeeMessage, OurEmployeeMessageAdmin)

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


#Админка - подписчики на вакансии
class SuscribeUserSVModelAdmin(admin.ModelAdmin):
    list_display = ('id','userName','userEmail','dateToSubscribe','isSubscribe')
    list_display_links = ('id', 'userName',)
    list_editable = ('isSubscribe',)
    readonly_fields = ('dateToSubscribe',)
    search_fields = ('userName', 'userEmail',)
    search_help_text = 'Поиск по подписчикам'
admin.site.register(SuscribeUserSVModel, SuscribeUserSVModelAdmin)

#Админка - соискатели на вакансию
class UserSendCVModelAdmin(admin.ModelAdmin):
    list_display = ('id','userName','userLocation','userTell','userEmail','dateSend')
    list_display_links = ('id', 'userName',)
    readonly_fields = ('userMessage','userTell','userEmail','dateSend',)
    search_fields = ('userName', 'userEmail',)
    search_help_text = 'Поиск по соискателям'
    list_filter = ('dateSend',)


admin.site.register(UserSendCVModel, UserSendCVModelAdmin)

#Админка - ссылки на соцсети
class OurSocLinksAdmin(admin.ModelAdmin):
    list_display = ('id','name','nameLink','getAllimg')
    list_display_links = ('id', 'name', 'nameLink')
    readonly_fields = ('getAllimg',)
    def getAllimg(self, object):
        return mark_safe(
            f"<img src='{object.imgLink_1.url}' width=75> <img src='{object.imgLink_2.url}' width=75><img src='{object.imgLink_2_hover.url}' width=75>")
    getAllimg.short_description = 'Фото'
admin.site.register(OurSocLinks, OurSocLinksAdmin)

#Админка - слайдер истории -OurHistory
class OurHistorySliderAdminInline(admin.TabularInline):
    model = OurHistorySlider
    classes = ('collapse',)
    readonly_fields = ('gethistorySliderPhoto',)
    extra = 1
    def gethistorySliderPhoto(self, object):
        if object.historySliderPhoto:
            return mark_safe(f"<img src='{object.historySliderPhoto.url}' width=150>")
    gethistorySliderPhoto.short_description = 'Фото'
class OurHistoryAdmin(admin.ModelAdmin):
    list_display = ('id','dateHistory','isPublished')
    list_display_links = ('id','dateHistory',)
    list_editable = ('isPublished',)
    inlines = (OurHistorySliderAdminInline,)
    ordering = ['-dateHistory']
admin.site.register(OurHistory, OurHistoryAdmin)

#Админка - фотографии для слайдера - OurHistorySlider
class OurHistorySliderAdmin(admin.ModelAdmin):
    list_display = ('id','title','history','publishedSlider','gethistorySliderPhoto')
    list_display_links = ('id','title')
    list_editable = ('publishedSlider',)
    ordering = ['history']
    list_filter = ('history', 'publishedSlider')
    readonly_fields = ('gethistorySliderPhoto',)
    def gethistorySliderPhoto(self, object):
        if object.historySliderPhoto:
            return mark_safe(f"<img src='{object.historySliderPhoto.url}' width=150>")
    gethistorySliderPhoto.short_description = 'Фото'
admin.site.register(OurHistorySlider, OurHistorySliderAdmin)


