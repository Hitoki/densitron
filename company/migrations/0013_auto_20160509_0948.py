# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_opportunity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='photo',
            field=models.ImageField(blank=True, help_text='Best size: 396px/296px. Min-width: 396px, Min-height: 296px.', null=True, upload_to='images'),
        ),
    ]
