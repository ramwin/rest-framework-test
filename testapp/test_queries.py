#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-05-21 17:07:05

import sys
# import datetime
# import pytz

from django.core.management.base import OutputWrapper
from django.core.management.color import color_style

from django.db.models import F
from testapp import head, head1, list1, list2, info
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
head("# 准备测试queryset")


class DateTimeTestCase(TestCase):

    def setUp(self):
        head1("## 准备测试时间的过滤和排序")
        self.test_date_list = [
            "2018-05-20T23:59:59+08:00",  # 2018-05-20T15:59:59+00:00"
            "2018-05-21T00:00:00+08:00",  # 2018-05-20T16:00:00+00:00"
            "2018-05-21T23:59:59+08:00",  # 2018-05-21T15:59:59+00:00
            "2018-05-22T00:00:00+08:00",  # 2018-05-21T16:00:00+00:00
            "2018-05-22T00:00:00+00:00",  # 2018-05-22T00:00:00+00:00
            "2018-05-22T23:00:00+08:00",  # 2018-05-22T15:00:00+00:00
        ]
        for date in self.test_date_list:
            datetime_obj = DateTimeModel.objects.create(time=date)
            info(datetime_obj)

    def test_datetimefield_filter_date(self):
        head1("### 准备测试通过`_date`来过滤时间")
        list1("* 普通时间直接过滤2018-05-21")
        queryset = DateTimeModel.objects.filter(time__date="2018-05-21")
        for instance in queryset:
            info(instance)
        info("返回了当前时区下时间为2018-05-21的时间")
        # new_date = timezone.now() - timezone.timedelta(0, 12*3600)
        new_date = timezone.datetime(2018,5,21,23,0,0,0,timezone.utc)
        info(new_date)
        list2("* utc时间下2018-05-21 23:00:00.date过滤")
        date = new_date.date()
        info(date)
        queryset2 = DateTimeModel.objects.filter(time__date=new_date.date())
        for instance in queryset2:
            info(instance)
        list2("* utc时间下2018-05-21 23:00:00用时间直接过滤")
        queryset3 = DateTimeModel.objects.filter(time__date=new_date)
        for instance in queryset3:
            info(instance)
        info("直接输入时间，会先把先把时间转化成本地时区，然后再过滤")
        list2("* 当地时区下过滤")

    def test_datetimefield_order(self):
        head1("### 准备测试时间的排序")


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
