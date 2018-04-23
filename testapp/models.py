# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.gis.db import models as gismodels

# Create your models here.


class BasicModel(models.Model):
    text = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "BasicModel: {}, id: {}".format(self.text, self.id)


class PartialModel(models.Model):
    """测试序列化类必须填写"""
    text1 = models.CharField(max_length=255)
    text2 = models.CharField(max_length=255)
    text3 = models.CharField(max_length=255)


class MyModel(models.Model):
    field = models.CharField(max_length=255)

    def __str__(self):
        return "MyModel: id:{}".format(self.id)

    class Meta:
        verbose_name_plural = "简单的MyModel"


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

    def __str__(self):
        return "GetOrCreate: Id:{}".format(self.id)


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


class TestAdminModel(models.Model):

    img = models.URLField()

    @property
    def avatar(self):
        from django.utils.html import format_html
        return format_html('<img src="{}" style="width: 130px; \
                            height: 100px"/>'.format(self.img))


class TestFilterModel(models.Model):
    text = models.ForeignKey(BasicModel, null=True)
    status = models.IntegerField(default=1)
    content = models.TextField(blank=True)
    many = models.ManyToManyField(MyModel, blank=True)  # 如果参数有many=1&many=2 那就会过滤many=1或者many=2都返回
    many2 = models.ManyToManyField(GetOrCreateModel, through="TestFilterThrough")  # 如果参数里面有many2=2就会过滤包含many2 = many2的

    class Meta:
        verbose_name_plural = "测试过滤的Model"

    def __str__(self):
        return "测试过滤;id:{};text:{}".format(self.id, self.content)


class TestFilterThrough(models.Model):
    model1 = models.ForeignKey(TestFilterModel)
    model2 = models.ForeignKey(GetOrCreateModel)

    class Meta:
        verbose_name_plural = "测试过滤的中间键through"
