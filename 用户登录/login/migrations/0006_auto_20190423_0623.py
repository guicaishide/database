# Generated by Django 2.2 on 2019-04-23 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20190423_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publish',
            old_name='pname',
            new_name='name',
        ),
    ]
