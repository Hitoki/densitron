# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20160211_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='application',
            field=models.ManyToManyField(blank=True, to='products.Application'),
        ),
    ]
