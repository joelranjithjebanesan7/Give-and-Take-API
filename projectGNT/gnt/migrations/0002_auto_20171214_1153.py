# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gnt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giveoffer',
            name='giver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gnt.Profile'),
        ),
    ]