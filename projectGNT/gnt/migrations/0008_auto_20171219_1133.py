# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gnt', '0007_takeoffer_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takeoffer',
            name='reason',
            field=models.CharField(max_length=200),
        ),
    ]