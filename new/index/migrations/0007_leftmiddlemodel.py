# Generated by Django 2.2 on 2019-04-25 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_remove_leftmodel_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeftMiddleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'leftmiddle',
            },
        ),
    ]
