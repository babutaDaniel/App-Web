# Generated by Django 3.2.7 on 2021-11-19 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_movies', '0003_auto_20211112_1137'),
    ]

    operations = [

        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
