# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class BasicModel(models.Model):
    text = models.CharField(max_length=255)


class MyModel(models.Model):
    field = models.CharField(max_length=255)


class FileModel(models.Model):
    fil = models.FileField(upload_to='uploads/%Y/%m/%d/')
    integer = models.IntegerField(default=0)


class ManyModel(models.Model):
    texts = models.ManyToManyField(BasicModel)
