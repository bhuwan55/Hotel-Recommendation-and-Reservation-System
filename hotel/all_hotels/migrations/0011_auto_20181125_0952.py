# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-25 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_hotels', '0010_auto_20181125_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='delux',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
