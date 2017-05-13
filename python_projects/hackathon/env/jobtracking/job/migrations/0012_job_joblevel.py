# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_job_userrequired'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='jobLevel',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'User'), (3, 'Supervisor')], default=2),
        ),
    ]
