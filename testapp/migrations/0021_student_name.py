# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0020_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]