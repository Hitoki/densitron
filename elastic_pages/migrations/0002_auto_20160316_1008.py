# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-16 10:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elastic_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pageworldpayscreenblock',
            options={'verbose_name': 'Slider panel'},
        ),
        migrations.AlterModelOptions(
            name='postsgalleryblock',
            options={'verbose_name': '3 Promo Panel'},
        ),
    ]