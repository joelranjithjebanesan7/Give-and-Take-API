# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 10:08
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gnt', '0004_auto_20171214_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]