#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-09-05 12:03:51


from rest_framework import serializers
from django.core.validators import MaxValueValidator
from . import models


class BasicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasicModel
        fields = "__all__"

    def to_representation(self, instance):
        # import ipdb
        # ipdb.set_trace()
        # if self.context['request'].user.level <= instance.userl.level:
        #     self.fields.pop('mobile_phone')
        return super(BasicModelSerializer, self).to_representation(instance)


class MyValidator(object):

    def __call__(self, value):
        print('calling validator')
        if value != 2:
            print("%s不是2呢" % value)
            raise serializers.ValidationError("不是2哦")


class MyField(serializers.RegexField):
    # validators = [MyValidator]
    regex = r'\d+'

    def __init__(self, **kwargs):
        super(MyField, self).__init__(self.regex, **kwargs)
        validator = MyValidator()
        self.validators.append(validator)

    def to_internal_value(self, data):
        print('calling to_internal_value')
        self.run_validators(data)
        print("转化数据")
        return "处理后的数据"


class MySerializer(serializers.Serializer):
    field = MyField()

    class Meta:
        model = models.MyModel
        fields = ['field']


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FileModel
        fields = ["fil"]
