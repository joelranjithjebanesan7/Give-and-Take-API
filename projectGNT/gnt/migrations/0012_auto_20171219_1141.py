# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gnt', '0011_auto_20171219_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takeoffer',
            name='pickup_timeslots',
            field=models.DateField(),
        ),
    ]
