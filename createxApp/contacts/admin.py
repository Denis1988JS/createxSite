from django.contrib import admin

from contacts.models import Contacts


# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id','name','userEmail','interesting','location','date')
    list_display_links = ('id','name','userEmail')
    list_filter = ('interesting','location','date')
admin.site.register(Contacts,ContactsAdmin)