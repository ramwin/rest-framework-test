# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0019_auto_20181127_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ManyToManyField(related_name='_student_friends_+', to='testapp.Student')),
            ],
        ),
    ]