# Generated by Django 2.2.24 on 2025-02-08 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='flat',
            new_name='flats',
        ),
    ]
