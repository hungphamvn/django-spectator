# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-01 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectator_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]