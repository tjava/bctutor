# Generated by Django 2.2 on 2020-06-03 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20200602_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
