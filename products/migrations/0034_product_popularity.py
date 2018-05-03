# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-23 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20160222_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='popularity',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (4, 5)], default=3, max_length=1),
        ),
    ]
