# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-17 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20160217_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
        migrations.AddField(
            model_name='faq',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]
