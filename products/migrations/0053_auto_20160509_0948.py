# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0052_auto_20160428_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(help_text='Best size: 70 px / 70 px. Max-height: 70 px.', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(help_text='Best size: 678 px / 396 px. Min-width: 248 px', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(help_text='Best size: 640 px / 218 px. Min-height: 218 px.', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='subservice',
            name='image',
            field=models.ImageField(help_text='Best size: 640 px / 218 px. Min-height: 218 px.', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='image',
            field=models.ImageField(help_text='Best size: 640 px / 218 px. Min-height: 218 px.', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='thumbnail',
            field=models.ImageField(blank=True, help_text='Best size: 80 px / 80 px. Max-height: 80 px. Max-width: 160px.', null=True, upload_to='images'),
        ),
    ]