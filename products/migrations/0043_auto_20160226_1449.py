# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-26 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0042_service_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='commonly_used',
            field=models.ManyToManyField(related_name='commonly_used_category', to='products.Bullet'),
        ),
        migrations.AddField(
            model_name='category',
            name='commonly_used_in',
            field=models.ManyToManyField(blank=True, related_name='commonly_used_in_category', to='products.UsedIn'),
        ),
        migrations.AddField(
            model_name='technology',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
