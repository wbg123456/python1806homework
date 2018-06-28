# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-27 07:57
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('t7', '0002_auto_20180627_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='书名')),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]
