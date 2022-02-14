# Generated by Django 3.2.7 on 2021-11-26 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list_movies', '0006_auto_20211126_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='first_image',
        ),
        migrations.AlterField(
            model_name='product',
            name='profile_image',
            field=models.ImageField(upload_to='images/'),
        ),


    ]