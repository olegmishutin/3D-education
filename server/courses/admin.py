from django.contrib import admin
from .models import Course, Group

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Описание', {'fields': ['image', 'name', 'description']}),
        ('Группы курса', {'fields': ['groups']})
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Group)
