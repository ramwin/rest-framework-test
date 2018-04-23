# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-23 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0010_testfiltermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestFilterThrough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='testfiltermodel',
            name='many',
            field=models.ManyToManyField(to='testapp.MyModel'),
        ),
        migrations.AddField(
            model_name='testfilterthrough',
            name='model1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.TestFilterModel'),
        ),
        migrations.AddField(
            model_name='testfilterthrough',
            name='model2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.GetOrCreateModel'),
        ),
        migrations.AddField(
            model_name='testfiltermodel',
            name='many2',
            field=models.ManyToManyField(through='testapp.TestFilterThrough', to='testapp.GetOrCreateModel'),
        ),
    ]
