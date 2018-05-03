# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-27 09:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='images')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Team'),
        ),
    ]
