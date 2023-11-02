from django.contrib import admin
from django.utils.safestring import mark_safe

from createx.models import MainSliderModel, HeaderContent, OurCoreValues, OurPartners, OurClientsReviews, AskFromUser, UserSubscribe, \
    DiscussForUser


# Register your models here.
#Админка главный слайдер
class MainSliderModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','isPublished','getimageSlider')
    list_display_links = ('id','title')
    list_editable = ("isPublished",)
    readonly_fields = ("getimageSlider",)
    fieldsets = (
        (None, {
            "fields": ("title",("imageSlider", "getimageSlider"))  # В одну строку
        }),
    )
    def getimageSlider(self, object):
        if object.imageSlider:
            return mark_safe(f"<img src='{object.imageSlider.url}' width=250 height='auto'>")
    getimageSlider.short_description = 'Фото'
admin.site.register(MainSliderModel,MainSliderModelAdmin)


#Админка заголовки страниц
class HeaderContentAdmin(admin.ModelAdmin):
    list_display = ('id','title','getImage')
    list_display_links =  ('id','title','getImage')
    readonly_fields = ("getImage",)
    fieldsets = (
        (None, {
            "fields": (("title", "content"),)  # В одну строку
        }),
        (None, {
            "fields": (("img", "getImage"),)  # В одну строку
        }),
    )
    def getImage(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=250 height='auto'>")
    getImage.short_description = 'Фото'
admin.site.register(HeaderContent,HeaderContentAdmin)

#Админка - наши ценности - OurCoreValues
class OurCoreValuesAdmin(admin.ModelAdmin):
    list_display = ('id', 'titleCore', 'contentCore', 'getcoreIcon')
    list_display_links = ('id', 'titleCore')
    readonly_fields = ('getcoreIcon',)
    fieldsets = (
        (None, {
            "fields": (("titleCore", "contentCore"),)  # В встроку
        }),
        (None, {
            "fields": (("coreIcon", "getcoreIcon"),)  #В встроку
        }),
    )
    def getcoreIcon(self, object):
        if object.coreIcon:
            return mark_safe(f"<img src='{object.coreIcon.url}' width=50>")
    getcoreIcon.short_description = 'Логотип'
admin.site.register(OurCoreValues,OurCoreValuesAdmin)


#Админка - наши партнеры - OurPartners
class OurPartnersAdmin(admin.ModelAdmin):
    list_display = ('id','namePartners','getlogo')
    list_display_links = ('id', 'namePartners')
    prepopulated_fields = {'slug': ('namePartners',)}
    readonly_fields = ("getlogo",)
    def getlogo(self, object):
        if object.logo:
            return mark_safe(f"<img src='{object.logo.url}' width=100>")
    getlogo.short_description = 'Логотип'
admin.site.register(OurPartners,OurPartnersAdmin)

#Админка - отзывы от партнеров - OurClientsReviews
class OurClientsReviewsAdmin(admin.ModelAdmin):
    list_display = ('id','nameClient','nameCompany','getMainImg','getIconClient')
    list_display_links = ('id', 'nameClient', 'nameCompany')
    readonly_fields = ("getMainImg",'getIconClient')
    fieldsets = (
        (None, {
            "fields": (("nameClient", "nameCompany",'adressCompeny'),)  # В встроку
        }),
        (None, {
            "fields": (("contentReview",),)  # В встроку
        }),
        (None, {
            "fields": (("getMainImg", "getIconClient"),)  # В встроку
        }),
        (None, {
            "fields": (("iconClient", "mainImg"),)  # В встроку
        }),
    )
    def getMainImg(self, object):
        if object.mainImg:
            return mark_safe(f"<img src='{object.mainImg.url}' width=100>")
    getMainImg.short_description = 'Фотография'
    def getIconClient(self, object):
        if object.iconClient:
            return mark_safe(f"<img src='{object.iconClient.url}' width=100>")
    getIconClient.short_description = 'Логотип'
admin.site.register(OurClientsReviews,OurClientsReviewsAdmin)


#Данные с форм
#Админка - вопросы от пользователей - AskFromUser
class AskFromUserAdmin(admin.ModelAdmin):
    list_display = ('id','userName','phoneNumberUser','date')
    list_display_links = ('id', 'userName')
    search_fields = ('userName', 'phoneNumberUser','askContent')
    search_help_text = ('Поиск по вопросам от пользователей')
admin.site.register(AskFromUser,AskFromUserAdmin)

#Админка - наши подписчики - UserSubscribe
class UserSubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'userEmail', 'date')
    list_display_links = ('id', 'userEmail')
    search_help_text = ('Поиск по подписчикам')
    search_fields = ('userEmail', 'date')
admin.site.register(UserSubscribe,UserSubscribeAdmin)

#Админка - обсуждение с пользователями - DiscussForUser
class DiscussForUserAdmin(admin.ModelAdmin):
    list_display = ('id','userName','phoneNumberUser','emailUser','date','userAgree')
    list_display_links = ('id','userName','phoneNumberUser','emailUser')
    search_fields = ('userName', 'emailUser')
    search_help_text = ('Поиск')
admin.site.register(DiscussForUser,DiscussForUserAdmin)


admin.site.site_title = "Createx Company"
admin.site.site_header = "Createx Company"


