from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'last_name')
    list_filter = ('is_staff', 'is_superuser')


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
