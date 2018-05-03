# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20160219_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationKit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('overview', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('hardware_features', models.ManyToManyField(blank=True, related_name='hardware_features', to='products.Feature')),
                ('software_features', models.ManyToManyField(blank=True, related_name='software_features', to='products.Feature')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=14),
        ),
        migrations.AddField(
            model_name='product',
            name='evaluation_kit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.EvaluationKit', verbose_name='Evaluation Kit'),
        ),
    ]