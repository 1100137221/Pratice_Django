# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 02:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_weather_bank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='bank',
        ),
    ]
