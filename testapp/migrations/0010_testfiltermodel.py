# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-19 01:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0009_testadminmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestFilterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1)),
                ('content', models.TextField(blank=True)),
                ('text', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.BasicModel')),
            ],
        ),
    ]
