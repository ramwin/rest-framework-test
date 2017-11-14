#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-09-21 15:16:54


from django.test import TestCase
from . import serializers
from .models import *


class MySerializerTestCase(TestCase):

    def test_serializer(self):
        print("准备测试")
        a = serializers.MySerializer(data={'field': 2})
        a.is_valid(raise_exception=True)
        a.save()

    def test_many(self):
        print("准备测试多对多")
        a = serializers.ManySerializer(data={'texts': ['a','b','c']})
        a.is_valid(raise_exception=True)
        a.save(texts=[])
        BasicModel.objects.create(text='text')
        a.instance.texts.add(*BasicModel.objects.all())
        print(serializers.ManyDetailSerializer(a.instance).data)
