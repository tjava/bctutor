# Generated by Django 2.2 on 2020-06-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20200601_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='dp',
            field=models.ImageField(blank=True, upload_to='dp'),
        ),
    ]
