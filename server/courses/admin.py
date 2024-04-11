from django.contrib import admin
from .models import Course, Group


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    fieldsets = [
        ('Описание', {'fields': ['image', 'name', 'description']}),
        ('Группы курса', {'fields': ['groups']})
    ]
    search_fields = ('name',)
    list_filter = ('groups',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Group, GroupAdmin)
