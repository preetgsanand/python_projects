# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='Please Add Description', max_length=1000),
        ),
    ]
