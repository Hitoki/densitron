# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-15 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20160315_1341'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.TextField()),
                ('first_name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64)),
                ('job_title', models.CharField(max_length=64)),
                ('comments', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('to_email', models.CharField(max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.ContactUser')),
            ],
        ),
        migrations.RemoveField(
            model_name='emailmessage',
            name='user',
        ),
        migrations.DeleteModel(
            name='EmailMessage',
        ),
    ]
