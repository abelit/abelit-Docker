# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-21 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20171221_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostmetric',
            name='cpu_load',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='hostmetric',
            name='disk_usage',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='hostmetric',
            name='memory_usage',
            field=models.CharField(blank=True, max_length=45),
        ),
    ]
