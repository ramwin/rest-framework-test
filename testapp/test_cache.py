#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-12-20 17:17:18


import time

from django.test import TestCase, Client

from testapp import head, head1, list1, list2, info
from testapp import service


class CacheTestCase(TestCase):

    def setUp(self):
        head("# 准备测试缓存")
        pass

    def test_cache_control(self):
        head1("## 准备测试cache_control")
        info("不可以使用cache_control来缓存函数")
        start = time.time()
        service.slow_function(3)
        end = time.time()
        info("第一次执行`slow_function`的时间: {}".format(end-start))
        start = time.time()
        service.slow_function(3)
        end = time.time()
        info("第二次执行`slow_function`的时间: {}".format(end-start))
