#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-06-07 17:49:05

import sys
import datetime
import pytz

from django.core.management.base import OutputWrapper
from django.core.management.color import color_style

from django.test import TestCase
from testapp import models, filters
from django.utils import timezone


out = OutputWrapper(sys.stdout)
style = color_style()


class FilterTestCase(TestCase):

    def setUp(self):
        out.write(style.MIGRATE_HEADING("准备测试过滤功能"))
        datas = [
            [
                {"_bool": _bool, "_int": _int}
                for _int in [0, 1, -1]
            ]
            for _bool in [True, False, None]
        ]
        for data_1 in datas:
            for data in data_1:
                print(data)
                models.TestFilterModel2.objects.create(**data)

    def test_method_filter(self):
        qs = filters.TestMethodFilter({"_bool": False}, models.TestFilterModel2.objects.all()).qs
        out.write(style.HTTP_INFO(qs))
