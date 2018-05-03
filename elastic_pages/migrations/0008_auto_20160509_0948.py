# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elastic_pages', '0007_auto_20160428_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='extra_meta_data',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bespokescreenblock',
            name='background',
            field=models.ImageField(help_text='Best size: 1440 px / 300 px. Min-width: 1440 px', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='pageheaderblock',
            name='logo_image',
            field=models.ImageField(help_text='Best size: 118 px / 67 px. Min-width: 118 px, Min-height: 67 px.', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='pageheadsoclink',
            name='soc_image',
            field=models.ImageField(help_text='Best size: 25 px / 25 px. Min-width: 25 px, Min-height: 25 px.', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='pagemainblock',
            name='background_image',
            field=models.ImageField(help_text='Best size: 640 px / 218 px. Min-height: 218 px.', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='postsgalleryblock',
            name='image_left',
            field=models.ImageField(help_text='Best size for all images: 476 px / 266 px. ', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='postsgalleryblock',
            name='image_middle',
            field=models.ImageField(help_text='Best size for all images: 476 px / 266 px. ', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='postsgalleryblock',
            name='image_right',
            field=models.ImageField(help_text='Best size for all images: 476 px / 266 px. ', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='textphotoblock',
            name='left_photo',
            field=models.ImageField(help_text='Best size: 278 px / 206 px.', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='textphotoblock',
            name='right_photo',
            field=models.ImageField(help_text='Best size: 278 px / 206 px.', upload_to='images'),
        ),
    ]