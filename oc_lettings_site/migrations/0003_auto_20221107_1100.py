# Generated by Django 3.0 on 2022-11-07 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_auto_20221105_1028'),
        ('profiles', '0002_auto_20221105_1541'),
     ]

    operations = [
        migrations.DeleteModel('Profile'),
        migrations.DeleteModel('Address'),
        migrations.DeleteModel('Letting'),

    ]
