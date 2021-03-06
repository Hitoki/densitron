# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-17 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_auto_20160217_0942'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='controller',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='feature',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='interface',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='os',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='structure',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='tftif',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='touchif',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='product',
            name='resolution',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Resolution'),
        ),
        migrations.AlterField(
            model_name='product',
            name='viewing_angle',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Viewing Angle (U/D/L/R)'),
        ),
    ]
