from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
# Register your models here.
from  news.models import CategoryNews, NewsModel,NewsCommentsModefl

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import  CKEditorUploadingWidget

class NewsModelAdminForm(forms.ModelForm):
    content = forms.CharField(label ="Контент",widget=CKEditorUploadingWidget())
    class Meta:
        model = NewsModel
        fields = ('content',)

class NewsModelInline(admin.TabularInline):
    model = NewsModel
    classes = ('collapse',)
    readonly_fields = ('getImg',)
    extra = 1
    def getImg(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=100>")
    getImg.short_description = 'Главное фото'

#Админка - категории новостей CategoryNews
class CategoryNewsAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name',)
    inlines = (NewsModelInline,)
    ordering = ['id']
admin.site.register(CategoryNews,CategoryNewsAdmin)

#Админка - новости NewsModel
class NewsCommentsModelInline(admin.TabularInline):
    model = NewsCommentsModefl
    classes = ('collapse',)
    readonly_fields =  ('date_publish',)
    extra = 1

class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','date_publish','categoryID','is_published','getImg')
    list_display_links = ('id','title',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('categoryID','date_publish','is_published',)
    search_fields = ('title', 'categoryID')
    search_help_text = ('Поиск по новостям')
    readonly_fields = ('getImg','date_publish',)
    inlines = (NewsCommentsModelInline,)
    form = NewsModelAdminForm
    fieldsets = (
        (None, {
              "fields": ('date_publish',("title", "slug",'categoryID','is_published'))#В одну строку
        }),
        (None, {
            "fields": (("img", "getImg",),)  # В одну строку
        }),
        (None, {
            "fields": (("content", ),)  # В одну строку
        }),
    )
    def getImg(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=100>")
    getImg.short_description = 'Главное фото'
admin.site.register(NewsModel,NewsModelAdmin)

#Админка - комментарии к новостям NewsCommentsModefl
class NewsCommentsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'user_email', 'parent', 'news', 'date_publish','is_published')
    list_display_links = ('id', 'user_name',)
    list_filter = ('news', 'is_published', 'date_publish',)
    search_fields = ('user_name', 'user_email','news',)
    search_help_text = ('Поиск по комментариям')
    readonly_fields = ('date_publish',)
    ordering = ['parent']

admin.site.register(NewsCommentsModefl,NewsCommentsModelAdmin)