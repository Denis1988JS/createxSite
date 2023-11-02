from django.contrib import admin
from django.utils.safestring import mark_safe

from services.models import OurServices, OurBenefits, ourOfferServices


# Register your models here.
class OurBenefitsAdmin(admin.ModelAdmin):
    # Админка - OurBenefits - наше преимущество
    list_display = ('id','title','content','getIcon')
    list_display_links = ('id', 'title')
    readonly_fields = ('getIcon',)
    fieldsets = (
        (None, {
            "fields": (("title", "content"),)  # В встроку
        }),
        (None, {
            "fields": (("icon", "getIcon"),)  # В встроку
        }),
    )
    def getIcon(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' width=50>")
    getIcon.short_description = 'Фото'
admin.site.register(OurBenefits,OurBenefitsAdmin)


# Админка - наши услуги - модель services
class OurOfferServicesInline(admin.TabularInline):
    model = ourOfferServices
    classes = ('collapse',)
    extra = 1
class OurServicesAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','is_active','getservicesOfferImg','getPhotoservicesImg')
    list_display_links = ('id', 'title', 'slug' )
    list_editable = ("is_active",)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (OurOfferServicesInline,)
    readonly_fields = ('getIcon','getIcon_hover','getPhotoservicesImg','getservicesOfferImg')
    fieldsets = (
        (None, {
              "fields": ("content", ("title", "slug",'is_active'))#В одну строку
        }),
        (None, {
            "fields": (("icon", "getIcon",),)  # В одну строку
        }),
        (None, {
            "fields": (("icon_hover", "getIcon_hover",),)  # В одну строку
        }),
        (None, {
            "fields": (("servicesOfferImg", "getservicesOfferImg",),)  # В одну строку
        }),
        (None, {
            "fields": (("servicesImg", "getPhotoservicesImg",),)  # В одну строку
        }),
    )

    def getIcon(self, object):
        if object.icon and object.icon_hover:
            return mark_safe(f"<img src='{object.icon.url}' width=100><img src='{object.icon_hover.url}' width=100>")
    getIcon.short_description = 'Иконка №1'

    def getIcon_hover(self, object):
        if object.icon_hover:
            return mark_safe(f"<img src='{object.icon_hover.url}' width=100")
    getIcon_hover.short_description = 'Иконка №2 hover'

    def getPhotoservicesImg(self, object):
        if object.servicesImg :
            return mark_safe(f"<img src='{object.servicesImg.url}' width=100")
    getPhotoservicesImg.short_description = 'Фото'

    def getservicesOfferImg(self, object):
        if object.servicesOfferImg:
            return mark_safe(f"<img src='{object.servicesOfferImg.url}' width=100>")
    getservicesOfferImg.short_description = 'Фото - offer'

admin.site.register(OurServices,OurServicesAdmin)

#Админка - ourOfferServices - наша оферта к услуге
class OurOfferServicesAdmin(admin.ModelAdmin):
    list_display = ('id','titleOffer','contentOffer','servicesID')
    list_display_links = ('id', 'titleOffer')
admin.site.register(ourOfferServices,OurOfferServicesAdmin)


