# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_auto_20170401_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='department',
            field=models.IntegerField(choices=[(1, 'School Education & Literacy'), (2, 'Higher Education'), (3, 'States/UTS')], default=1),
        ),
    ]
