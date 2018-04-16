# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.gis.db import models as gismodels

# Create your models here.


class BasicModel(models.Model):
    text = models.CharField(max_length=255, blank=False)


class PartialModel(models.Model):
    """测试序列化类必须填写"""
    text1 = models.CharField(max_length=255)
    text2 = models.CharField(max_length=255)
    text3 = models.CharField(max_length=255)


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


def myfunction():
    print("调用myfunction")
    return "123"


class TestDefault(models.Model):
    """测试default的函数是否会被调用"""
    text = models.CharField(default=myfunction, max_length=32)


class TestNullModel(models.Model):
    can_null_blank = models.TextField(null=True, blank=True)
    can_null = models.TextField(null=True)  # 可以不填或填None，不能填 ""
    can_blank = models.TextField(blank=True)  # 可以不填或填"", 不能填 None
    can_default = models.TextField(default="")  # 可以不填, 但是不能为空或者None
    can = models.TextField()  # 必填, 不能为空


class ForeignKeyModel2(models.Model):
    """测试上传用外键，下载用字典"""
    text = models.ForeignKey(BasicModel, null=True)


class TestMethodModel(models.Model):
    text = models.CharField(max_length=243)

    def get_num(self):
        return 2


class ValidateModel(models.Model):
    STATUS_CHOICE = (
        (0, "以支付"),
        (1, "为支付"),
    )
    status = models.IntegerField(choices=STATUS_CHOICE)


class TestPropertyModel(models.Model):

    @property  # 很好，这个就是read_only的，直接用
    def pro(self):
        return "我的属性"
