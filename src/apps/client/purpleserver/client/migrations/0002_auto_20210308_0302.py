# Generated by Django 3.1.7 on 2021-03-08 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='user',
            new_name='created_by',
        ),
    ]
