# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-19 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_auto_20160219_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publicated',
            field=models.DateField(blank=True, null=True),
        ),
    ]
