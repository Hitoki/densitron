# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-28 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_people_place_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['place_priority']},
        ),
        migrations.AlterModelOptions(
            name='people',
            options={'ordering': ['job__place_priority', 'place_priority']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['place_priority']},
        ),
        migrations.AddField(
            model_name='job',
            name='place_priority',
            field=models.SmallIntegerField(default=1, help_text='Display priority list. 1 - top, 2+ - bottom. (max 32767)'),
        ),
        migrations.AddField(
            model_name='team',
            name='place_priority',
            field=models.SmallIntegerField(default=1, help_text='Display priority list. 1 - top, 2+ - bottom. (max 32767)'),
        ),
        migrations.AlterField(
            model_name='people',
            name='place_priority',
            field=models.SmallIntegerField(default=1, help_text='Display priority list. 1 - top, 2+ - bottom. (max 32767)'),
        ),
    ]
