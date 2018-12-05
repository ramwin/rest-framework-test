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
    time = models.DateTimeField()  # 可以直接使用datetime对象

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
    # 如果是integer，不填的话就会变成None
    can_null_blank_integer = models.IntegerField(null=True, blank=True)


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
    # 如果参数有 many=1&many=2 那就会过滤many=1或者many=2都返回
    many = models.ManyToManyField(MyModel, blank=True)
    # 如果参数里面有 many2=2就会过滤包含many2 = many2的
    many2 = models.ManyToManyField(
        GetOrCreateModel, through="TestFilterThrough")

    class Meta:
        verbose_name_plural = "测试过滤的Model"

    def __str__(self):
        return "测试过滤;id:{};text:{}".format(self.id, self.content)


class TestFilterThrough(models.Model):
    model1 = models.ForeignKey(TestFilterModel)
    model2 = models.ForeignKey(GetOrCreateModel)

    class Meta:
        verbose_name_plural = "测试过滤的中间键through"


class TestOneToOneField(models.Model):
    text = models.OneToOneField(
        BasicModel, on_delete=models.CASCADE, null=True)


class TestFilterModel2(models.Model):
    _bool = models.NullBooleanField()
    _int = models.IntegerField()

    def __str__(self):
        return "boll: {}, int: {}".format(self._bool, self._int)


class TestMethodTriggerModel(models.Model):

    text = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "BasicModel: {}, id: {}".format(self.text, self.id)

    def save(self, *args, **kwargs):
        print("TestMethodTriggerModel.save触发")
        return super(TestMethodTriggerModel, self).save(*args, **kwargs)


class TestUniqueModel(models.Model):
    """如果有null=True,就可以随便，否则就会报错。空字符串也是值"""
    text1 = models.CharField(max_length=42, unique=True)
    text2 = models.CharField(max_length=42, unique=True, blank=True)
    text3 = models.CharField(max_length=42, unique=True, null=True)
    text4 = models.CharField(max_length=42, unique=True, blank=True, null=True)


class TestDecimalModel(models.Model):
    deci = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)

    class Meta:
        verbose_name_plural = "测试DecimalField"


class Student(models.Model):
    name = models.CharField(max_length=25)
    friends = models.ManyToManyField("self")

    def __str__(self):
        return self.name
