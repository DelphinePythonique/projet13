# Generated by Django 3.0 on 2022-11-05 15:41

from django.db import migrations


def transfer_old_profile_in_new_table(oldprofile, Profile2):

    newprofile = Profile2(
        id=oldprofile.id,
        user_id=oldprofile.user.id,
        favorite_city=oldprofile.favorite_city,
    )

    newprofile.save()


def add_datas(apps, schema_editors):

    Old_profile = apps.get_model("oc_lettings_site", "Profile")
    New_profile = apps.get_model("profiles", "Profile2")
    for old_profile in Old_profile.objects.all():
        transfer_old_profile_in_new_table(old_profile, New_profile)


def remove_datas(apps, schema_editors):

    NewProfile = apps.get_model("profiles", "Profile2")
    for new_letting in NewProfile.objects.all():
        new_letting.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0002_auto_20221105_1028"),
    ]

    operations = [migrations.RunPython(add_datas, remove_datas)]
