# Generated by Django 4.1.1 on 2022-11-06 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="gallery", new_name="card",),
    ]