# Generated by Django 3.0 on 2022-11-08 11:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_auto_20221105_1541'),

    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile2',
            new_name='Profile',
        ),
    ]
