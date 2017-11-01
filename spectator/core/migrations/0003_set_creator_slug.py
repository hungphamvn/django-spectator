# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-01 09:03
from __future__ import unicode_literals

from django.db import migrations

from spectator.core.fields import AutoSlugField


def set_slug(apps, schema_editor):
    """
    Create a slug for each Creator already in the DB.
    """
    Creator = apps.get_model('spectator_core', 'Creator')

    # We need to use AutoSlugField's methods to generate a slug for each
    # Creator.
    asfield = AutoSlugField(populate_from='name', separator='-')
    asfield.attname = 'slug'

    for c in Creator.objects.all():
        c.slug = asfield.pre_save(c, True)
        c.save()


class Migration(migrations.Migration):

    dependencies = [
        ('spectator_core', '0002_creator_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='slug',
            field=AutoSlugField(blank=True, default='slug', editable=False, populate_from='name'),
        ),
        migrations.RunPython(set_slug),
    ]
