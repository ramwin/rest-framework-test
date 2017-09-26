#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-09-21 15:16:54


from django.test import TestCase
from . import serializers


class MySerializerTestCase(TestCase):

    def test_serializer(self):
        print("准备测试")
        a = serializers.MySerializer(data={'field': 2})
        a.is_valid(raise_exception=True)
        a.save()
