# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('shift', models.IntegerField(choices=[(1, 'Morning'), (2, 'Evening')], default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateTimeField()),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(1, 'Lab'), (2, 'Lecture'), (3, 'Tutorial')], default=3)),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday')], default=1)),
                ('start', models.TimeField(auto_now=True)),
                ('end', models.TimeField(auto_now=True)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Batch')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('floor', models.CharField(blank=True, max_length=100)),
                ('category', models.IntegerField(choices=[(1, 'Administration'), (2, 'Lab'), (3, 'Lecture')], default=3)),
                ('assisstant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Entity')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Block')),
            ],
        ),
        migrations.AddField(
            model_name='period',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Room'),
        ),
        migrations.AddField(
            model_name='entity',
            name='role',
            field=models.ManyToManyField(to='users.Role'),
        ),
        migrations.AddField(
            model_name='batch',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Department'),
        ),
    ]
