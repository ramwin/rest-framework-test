#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-09-19 11:27:49


from __future__ import unicode_literals

import json
import sys

from django.test import TestCase
from django.core.management.base import OutputWrapper
from django.core.management.color import color_style

from testapp.models import *
from testapp.serializers import *
from testapp import head, head1, list1, list2, success, info

head("# 准备测试models")


class ModelTest(TestCase):

    def test_unique(self):
        info("准备测试unique")
        # TestUniqueModel.objects.create(text1='')
        # TestUniqueModel.objects.create(text1='')  # 报错，重复
        print(TestUniqueModel.objects.create(text1='', text2='', ).text3)
        print(TestUniqueModel.objects.create(text1='er', text2='text2').text4)  # 报错，重复

    def test_decimal(self):
        head1("# 准备测试decimal这个field")
        list1("* 测试基础的maxj_digits, decimal_palces超出会怎么样")
        data = {"deci": "0.333"}
        s = TestDecimalSerializer(data=data)
        s.is_valid()
        info(s.errors)
        info("如果数字数量超出了,会报错, 就算小数位数只有1分,整数部分仍然不能多一位, 反之整数部分小了,小数部分也不能变多")
        info("默认不能传入空字符串和None")
