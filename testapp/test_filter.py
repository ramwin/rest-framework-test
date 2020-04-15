#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-06-07 17:49:05

import sys

from django.core.management.base import OutputWrapper
from django.core.management.color import color_style
from django.test import Client

from django.test import TestCase
from testapp import models, filters
from testapp import head, head1, list1, list2, info


out = OutputWrapper(sys.stdout)
style = color_style()
list1("list1")
list2("list2")


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
                # print(data)
                models.TestFilterModel2.objects.create(**data)

    def test_method_filter(self):
        qs = filters.TestMethodFilter(
            {"_bool": 'true'}, models.TestFilterModel2.objects.all()).qs
        out.write(style.HTTP_INFO(qs))

    def test_multichoice_filter(self):
        head("# 准备测试multichoice filter")
        head1("## 过滤CharField")
        models.TestFilter.objects.create(
            _type="类型1")
        fenlei1 = models.BasicModel.objects.create(text="分类1")
        fenlei2 = models.BasicModel.objects.create(text="分类2")
        fenlei3 = models.BasicModel.objects.create(text="分类3")
        instance1 = models.TestFilter.objects.create(
            _type="类型1")
        instance2 = models.TestFilter.objects.create(
            _type="类型2")
        instance3 = models.TestFilter.objects.create(
            _type="类型3")
        instance1.basic_model.add(fenlei1)
        instance2.basic_model.add(fenlei2)
        instance3.basic_model.add(fenlei3)
        client = Client()
        info("找到类型1和类型2的")
        response = client.get(
            "/testapp/testfilter/?_type=类型1&_type=类型2",
            headers={"accept": "application/json"}
            )
        info(response.data)
        head1("## 过滤ManyToManyField")
        response = client.get(
            "/testapp/testfilter/?basic_model=1&basic_model=2",
            headers={"accept": "application/json"}
            )
        info(response.data)
        response = client.get(
            "/testapp/testfilter/?basic_model=1&basic_model=3",
            headers={"accept": "application/json"}
            )
        info(response.data)
