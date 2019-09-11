from django.contrib import admin

# Register your models here.

from . models import *
admin.site.register(Person)
class PublishAdmin(admin.ModelAdmin):
    list_display = ['name','address']
    search_fields = ['name']
    list_filter = ['address']
admin.site.register(Publish,PublishAdmin)
admin.site.register(Book)
