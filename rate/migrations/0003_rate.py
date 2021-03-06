# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countryName', models.TextField()),
                ('buyCashRate', models.FloatField()),
                ('sellCashRate', models.FloatField()),
                ('buySpotRate', models.FloatField()),
                ('sellSpotRate', models.FloatField()),
                ('lastModifyDate', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'rate',
            },
        ),
    ]
