# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20160212_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='lowpowerproduct',
            name='interface',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Interface'),
        ),
    ]
