# Generated by Django 3.2.7 on 2021-11-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='images/defaultUser - Copy.png', null=True, upload_to='profile_images/'),
        ),
    ]
