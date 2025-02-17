# Generated by Django 3.0 on 2022-11-05 14:03
from django.db import migrations


def transfer_old_letting_in_new_table(old_letting, new_address, NewLetting):
    newletting = NewLetting(
        id=old_letting.id,
        title=old_letting.title,
        address_id=new_address.id,
    )

    newletting.save()


def add_datas(apps, schema_editors):
    NewLetting = apps.get_model("lettings", "Letting")
    Old_letting = apps.get_model("oc_lettings_site", "Letting")
    NewAddress = apps.get_model("lettings", "Address")
    for old_letting in Old_letting.objects.all():
        new_address = NewAddress.objects.get(pk=old_letting.address.id)
        transfer_old_letting_in_new_table(old_letting, new_address, NewLetting)


def remove_datas(apps, schema_editors):

    NewLetting = apps.get_model("lettings", "Letting")
    for new_letting in NewLetting.objects.all():
        new_letting.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0002_auto_20221105_1035"),
    ]

    operations = [migrations.RunPython(add_datas, remove_datas)]
