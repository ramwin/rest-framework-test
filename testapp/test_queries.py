#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-05-21 17:07:05

import sys
# import datetime
# import pytz

from django.core.management.base import OutputWrapper
from django.core.management.color import color_style

from django.db.models import F
from django.test import TestCase
from testapp.models import DateTimeModel, PartialModel, BasicModel, \
    TestMethodTriggerModel
from django.utils import timezone


out = OutputWrapper(sys.stdout)
style = color_style()


class ColorfulLog(object):
    def info(self, text):
        out.write(style.HTTP_INFO(text))

    def log(self, text):
        out.write(style.HTTP_SUCCESS(text))


log = ColorfulLog()


class DateTimeTestCase(TestCase):

    def setUp(self):
        out.write(style.MIGRATE_HEADING("准备测试时间的过滤"))
        self.test_date_list = [
            "2018-05-20T23:59:59+08:00",  # 2018-05-20T15:59:59+00:00"
            "2018-05-21T00:00:00+08:00",  # 2018-05-20T16:00:00+00:00"
            "2018-05-21T23:59:59+08:00",  #
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


class ChangeDuringQuerysetTestCase(TestCase):
    """
    检测queryset循环中出现变更的问题
    python3 manage.py test testapp.test_queries.ChangeDuringQuerysetTestCase
    """

    def setUp(self):
        out.write(style.MIGRATE_HEADING("准备测试queryset循环中变化问题"))
        BasicModel.objects.all().delete()
        BasicModel.objects.create(text='text')
        BasicModel.objects.create(text='text')

    def test_change_during_for(self):
        out.write(style.HTTP_INFO("测试循环queryset中，model变更了怎么办"))
        queryset = BasicModel.objects.filter(text='text')
        index = 0
        for basicmodel in queryset:
            index += 1
            print("第{}个model: {}".format(index, basicmodel))
            basicmodel.refresh_from_db()
            print("更新后的model: {}".format(basicmodel))
            if index == 1:
                BasicModel.objects.filter(text='text').update(text='text1')
                print("更新了数据以后的数量: {}".format(queryset.count()))
            print("真正剩下的数量{}".format(
                BasicModel.objects.filter(text='text').count()))


class TestMethodTestCase(TestCase):
    """
    检测方法的触发
    python3 manage.py test testapp.test_queries.TestMethodTestCase
    """

    def setUp(self):
        log.info("准备测试一些方法的触发极致")
        TestMethodTriggerModel.objects.create(text='text')

    def test_update_trigger_save(self):
        log.log("测试update是否触发save")
        TestMethodTriggerModel.objects.update(text='text1')  # 并没有触发save
        log.log("触发了吗")


class ForeignKeyFilterTestCase(TestCase):

    def setUp(self):
        log.info("准备测试外键的过滤机制")
        log.info("暂时不测试了，之前做过，有文档")
