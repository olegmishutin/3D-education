# Generated by Django 5.0.4 on 2024-04-10 08:54

import users.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.managers.CustomUserManager()),
            ],
        ),
    ]