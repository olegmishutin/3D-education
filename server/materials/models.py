from django.db import models


class App(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='apps/', verbose_name='Изображение')
    href = models.URLField(verbose_name='Ссылка для скачивания')

    class Meta:
        db_table = 'App'
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'

    def __str__(self):
        return self.name


class HandBook(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='hand-books-image/', verbose_name='Изображение')
    file = models.FileField(upload_to='hand-books-files/', verbose_name='Файл (необязательно)', null=True, blank=True)

    class Meta:
        db_table = 'HandBook'
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'

    def __str__(self):
        return self.name
