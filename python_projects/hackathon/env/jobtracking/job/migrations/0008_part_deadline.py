# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='deadline',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
