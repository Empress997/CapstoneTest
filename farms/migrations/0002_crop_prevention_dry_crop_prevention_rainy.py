# Generated by Django 4.1.2 on 2022-10-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='prevention_dry',
            field=models.TextField(default=1, verbose_name='Control/Prevention Dry Season'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='prevention_rainy',
            field=models.TextField(default=1, verbose_name='Control/Prevention Rainy Season'),
            preserve_default=False,
        ),
    ]