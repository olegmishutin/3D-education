# Generated by Django 5.0.4 on 2024-04-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handbook',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='hand-books-files/', verbose_name='Файл (необязательно)'),
        ),
    ]
