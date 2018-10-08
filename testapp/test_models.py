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

def info(text):
    out.write(style.HTTP_INFO(text))


class ModelTest(TestCase):

    def test_unique(self):
        info("准备测试unique")
        # TestUniqueModel.objects.create(text1='')
        # TestUniqueModel.objects.create(text1='')  # 报错，重复
        print(TestUniqueModel.objects.create(text1='', text2='', ).text3)
        print(TestUniqueModel.objects.create(text1='er', text2='text2').text4)  # 报错，重复
