# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 13:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0051_technology_thumbnail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['priority'], 'verbose_name': 'Product Sub-Category', 'verbose_name_plural': 'Product Sub-categories'},
        ),
    ]
