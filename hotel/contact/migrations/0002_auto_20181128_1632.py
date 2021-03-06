# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-28 10:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('all_hotels', '0014_auto_20181128_1549'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancel_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('message', models.TextField(blank=True, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_hotels.Hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
