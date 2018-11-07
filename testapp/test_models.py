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


out = OutputWrapper(sys.stdout)
style = color_style()

def head(text):
    out.write(style.SQL_TABLE(text))

def head1(text):
    out.write(style.MIGRATE_HEADING(text))

def list1(text):
    out.write(style.SQL_FIELD(text))

def list2(text):
    out.write(style.SQL_COLTYPE(text))

def info(text):
    out.write(style.HTTP_INFO(text))



class ModelTest(TestCase):

    def test_unique(self):
        info("准备测试unique")
        # TestUniqueModel.objects.create(text1='')
        # TestUniqueModel.objects.create(text1='')  # 报错，重复
        print(TestUniqueModel.objects.create(text1='', text2='', ).text3)
        print(TestUniqueModel.objects.create(text1='er', text2='text2').text4)  # 报错，重复

    def test_decimal(self):
        head("准备测试decimal这个field")
        list1("* 测试基础的maxj_digits, decimal_palces超出会怎么样")
        data = {"deci": "0.333"}
        s = TestDecimalSerializer(data=data)
        s.is_valid()
        info(s.errors)
        info("如果数字数量超出了,会报错, 就算小数位数只有1分,整数部分仍然不能多一位, 反之整数部分小了,小数部分也不能变多")
        info("默认不能传入空字符串和None")
