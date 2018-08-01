#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-05-21 17:07:05

import sys
import datetime
import pytz

from django.core.management.base import OutputWrapper
from django.core.management.color import color_style

from django.db.models import F
from django.test import TestCase
from testapp.models import DateTimeModel, PartialModel
from django.utils import timezone


out = OutputWrapper(sys.stdout)
style = color_style()


class DateTimeTestCase(TestCase):

    def setUp(self):
        out.write(style.MIGRATE_HEADING("准备测试时间的过滤"))
        self.test_date_list = [
            "2018-05-20T23:59:59+08:00", # 2018-05-20T15:59:59+00:00"
            "2018-05-21T00:00:00+08:00", # 2018-05-20T16:00:00+00:00"
            "2018-05-21T23:59:59+08:00", # 
            "2018-05-22T00:00:00+08:00",
        ]
        for date in self.test_date_list:
            out.write(style.HTTP_INFO(date))
        for date in self.test_date_list:
            DateTimeModel.objects.create(time=date)

    def test_datetimefield_filter_date(self):
        queryset = DateTimeModel.objects.filter(time__date="2018-05-21")
        out.write(style.HTTP_SERVER_ERROR("普通时间过滤"))
        for instance in queryset:
            out.write(style.WARNING(instance.time))
        new_date = timezone.now() + timezone.timedelta(0, 12*3600)
        print(new_date)
        queryset2 = DateTimeModel.objects.filter(time__date=new_date.date())
        out.write(style.HTTP_SERVER_ERROR("utc时间过滤"))
        for instance in queryset2:
            out.write(style.WARNING(instance.time))


class ExpressionTestCase(TestCase):
    """使用PartialModel来测试Query Expression"""

    def setUp(self):
        self.model1 = PartialModel.objects.create(
            text1='text1', text2='text1')
        self.model2 = PartialModel.objects.create(
            text1='text1', text2='text2')

    def test_f(self):
        qs = PartialModel.objects.filter(text1=F('text2'))
        self.assertIn(self.model1, qs)
        self.assertNotIn(self.model2, qs)
