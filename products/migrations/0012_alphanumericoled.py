# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20160211_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlphanumericOLED',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('display_id', models.IntegerField(default=0)),
                ('module', models.CharField(max_length=128)),
                ('character_width', models.SmallIntegerField(default=0)),
                ('character_height', models.SmallIntegerField(default=0)),
                ('dimension_width', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('dimension_height', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('dimension_depth', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('viewing_area_width', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('viewing_area_height', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('active_area_width', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('active_area_height', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('screen_size', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('screen_diagonal', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('package_mode', models.CharField(blank=True, max_length=128, null=True)),
                ('duty', models.CharField(blank=True, max_length=128, null=True)),
                ('backlight_optional', models.BooleanField(default=False)),
                ('el', models.BooleanField(default=False)),
                ('edge_led', models.BooleanField(default=False)),
                ('smd_led', models.BooleanField(default=False)),
                ('cfl', models.BooleanField(default=False)),
                ('cfl_direct', models.BooleanField(default=False)),
                ('tft_size', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('tft_mode', models.CharField(blank=True, max_length=128, null=True)),
                ('tft_brightness', models.SmallIntegerField(default=0)),
                ('interface', models.CharField(max_length=128)),
                ('tft_backlight', models.CharField(blank=True, max_length=256, null=True)),
                ('tft_driving_board', models.CharField(blank=True, max_length=256, null=True)),
                ('tft_driving_board_link', models.CharField(blank=True, max_length=256, null=True)),
                ('tft_resolution', models.CharField(blank=True, max_length=256, null=True)),
                ('popup_text', models.CharField(blank=True, max_length=256, null=True)),
                ('display_country', models.SmallIntegerField(default=0)),
                ('display_country_include', models.BooleanField(default=True)),
                ('custom_field_1', models.CharField(blank=True, max_length=256, null=True)),
                ('custom_field_1_text', models.TextField(blank=True, null=True)),
                ('custom_field_1_set', models.BooleanField(default=False)),
                ('custom_field_2', models.CharField(blank=True, max_length=256, null=True)),
                ('custom_field_2_text', models.TextField(blank=True, null=True)),
                ('custom_field_2_set', models.BooleanField(default=False)),
                ('custom_field_3', models.CharField(blank=True, max_length=256, null=True)),
                ('custom_field_3_text', models.TextField(blank=True, null=True)),
                ('custom_field_3_set', models.BooleanField(default=False)),
                ('custom_field_4', models.CharField(blank=True, max_length=256, null=True)),
                ('custom_field_4_text', models.TextField(blank=True, null=True)),
                ('custom_field_4_set', models.BooleanField(default=False)),
                ('custom_field_5', models.CharField(blank=True, max_length=256, null=True)),
                ('custom_field_5_text', models.TextField(blank=True, null=True)),
                ('custom_field_5_set', models.BooleanField(default=False)),
                ('custom_field_6', models.CharField(blank=True, max_length=256, null=True)),
                ('custom_field_6_text', models.TextField(blank=True, null=True)),
                ('custom_field_6_set', models.BooleanField(default=False)),
                ('custom_field_7', models.CharField(blank=True, max_length=256, null=True)),
                ('custom_field_7_text', models.TextField(blank=True, null=True)),
                ('custom_field_7_set', models.BooleanField(default=False)),
                ('custom_field_8', models.CharField(blank=True, max_length=256, null=True)),
                ('custom_field_8_text', models.TextField(blank=True, null=True)),
                ('custom_field_8_set', models.BooleanField(default=False)),
                ('pdf_replacement_ektron_content_id', models.CharField(blank=True, max_length=256, null=True)),
                ('pdf_replacement_ektron_content_id_tabs', models.CharField(blank=True, max_length=256, null=True)),
                ('parent_id', models.SmallIntegerField(default=3)),
                ('display_type', models.SmallIntegerField(default=1)),
                ('ektron_content_id', models.SmallIntegerField(default=64)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='')),
                ('country_flag', models.SmallIntegerField(default=0)),
                ('country_include', models.BooleanField(default=True)),
                ('pdf_flag', models.SmallIntegerField(default=1)),
                ('pdf_country_include', models.BooleanField(default=False)),
                ('application', models.ManyToManyField(blank=True, to='products.Application')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
                ('commonly_used', models.ManyToManyField(related_name='alphanumeric_oled_commonly_used', to='products.Bullet')),
                ('commonly_used_in', models.ManyToManyField(blank=True, related_name='alphanumeric_oled_commonly_used_in', to='products.UsedIn')),
                ('spec', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Spec')),
                ('why_dens', models.ManyToManyField(related_name='alphanumeric_oled_why_dens', to='products.Bullet')),
            ],
        ),
    ]
