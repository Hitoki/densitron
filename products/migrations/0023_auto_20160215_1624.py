# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20160215_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touchpanelproduct',
            name='supported_os',
            field=models.ManyToManyField(blank=True, to='products.Os'),
        ),
    ]
