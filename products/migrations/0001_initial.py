# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('dimension_w', models.DecimalField(decimal_places=2, max_digits=6)),
                ('dimension_h', models.DecimalField(decimal_places=2, max_digits=6)),
                ('dimension_d', models.DecimalField(decimal_places=2, max_digits=6)),
                ('size', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Touch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=128)),
                ('i_f', models.CharField(max_length=32)),
                ('points', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='technology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Technology'),
        ),
        migrations.AddField(
            model_name='product',
            name='touch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Touch'),
        ),
    ]
