from django.contrib import admin
from .models import HandBook, App


class HandBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'file')
    search_fields = ('name',)


class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'href')
    search_fields = ('name', 'href')


admin.site.register(HandBook, HandBookAdmin)
admin.site.register(App, AppAdmin)
