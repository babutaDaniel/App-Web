# Generated by Django 3.2.7 on 2021-11-26 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 26, 12, 20, 21, 273881)),
        ),
    ]
