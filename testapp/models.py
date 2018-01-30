# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.gis.db import models as gismodels

# Create your models here.


class BasicModel(models.Model):
    text = models.CharField(max_length=255, blank=False)


class MyModel(models.Model):
    field = models.CharField(max_length=255)


class FileModel(models.Model):
    fil = models.FileField(upload_to='uploads/%Y/%m/%d/')
    integer = models.IntegerField(default=0)


class ManyModel(models.Model):
    texts = models.ManyToManyField(BasicModel)


class DateTimeModel(models.Model):
    time = models.DateTimeField()

    def __str__(self):
        return "id:%d, time: %s" % (self.id or 0, self.time)


# class PointModel(gismodels.Model):
#     point = gismodels.PointField()


class ForeignKeyModel(models.Model):
    text = models.ManyToManyField(BasicModel)


class GetOrCreateModel(models.Model):
    text = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
