from django.db import models
from users.models import User


class Group(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'Group'
        verbose_name = 'Группа курса'
        verbose_name_plural = 'Группы курсов'

    def __str__(self):
        return self.name

class Course(models.Model):
    image = models.ImageField(upload_to='courses/', verbose_name='Картинка')
    name = models.CharField(max_length=200, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    users = models.ManyToManyField(User, db_table='UserCourse', related_name='courses', verbose_name='Пользователи')
    groups = models.ManyToManyField(Group, db_table='CourseGroup', related_name='courses', verbose_name='Группа')

    class Meta:
        db_table = 'Course'
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name
