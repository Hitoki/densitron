# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20160215_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='lowpowerproduct',
            name='resolution',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]