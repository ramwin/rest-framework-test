#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-09-21 15:16:54


import sys

from django.test import TestCase
from django.core.management.base import OutputWrapper
from django.core.management.color import color_style
from . import serializers
from .models import *


out = OutputWrapper(sys.stdout)
style = color_style()
class MySerializerTestCase(TestCase):

    def test_serializer(self):
        print("准备测试")
        a = serializers.MySerializer(data={'field': 2})
        a.is_valid(raise_exception=True)
        a.save()

    def test_many(self):
        print("准备测试多对多")
        a = serializers.ManySerializer(data={'texts': ['1','2','3']})
        a.is_valid(raise_exception=True)
        # a.save(texts=[])
        a.save()
        print("保存成功")
        BasicModel.objects.create(text='text')
        a.instance.texts.add(*BasicModel.objects.all())
        # print(serializers.ManyDetailSerializer(a.instance).data)

    def test_null(self):
        print("准备测试null")
        data_list = [
            {},
            {"can": ""},
            {"can": "can"}, # 有null为null，有blank为""
            {"can": "can", "can_null": None},
            {"can": "can", "can_null": ""},
            {"can": "can", "can_blank": None},
            {"can": "can", "can_default": ""},
        ]
        for data in data_list:
            serializer = serializers.TestNullSerializer(data=data)
            print("准备处理: %s" % data)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                out.write(style.SUCCESS(serializer.data))
            else:
                out.write(style.ERROR(serializer.errors))
