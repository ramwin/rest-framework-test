# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_auto_20180425_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestOneToOneField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testapp.BasicModel')),
            ],
        ),
    ]