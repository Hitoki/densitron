# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-15 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20160308_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailmessage',
            name='user',
        ),
        migrations.DeleteModel(
            name='EmailMessage',
        ),
    ]
