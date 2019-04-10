#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-04-10 11:57:08


from django.test import Client
from django.test import TestCase

from testapp import head, head1, list1, list2, info


head("# 准备测试和urls有关的接口")
class ViewSetFilter(TestCase):

    def test_path(self):
        head1("\n## 测试使用path")
        list1("* 测试如果是int的converter遇到")
        client = Client()
        info("使用负数传入就不支持了")
        response = client.get("/testapp/testint/1/")
        self.assertEqual(response.resolver_match.kwargs, {"pk": 1})
        response = client.get("/testapp/testint/-1/")
        self.assertEqual(response.status_code, 404)
