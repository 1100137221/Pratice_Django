# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='bank',
            field=models.TextField(default=''),
        ),
    ]