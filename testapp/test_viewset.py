#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-03-28 16:48:33


from django.test import Client
from django.test import TestCase

from testapp import head, head1, list1, list2, info


class ViewSetFilter(TestCase):

    def test_viewset_post(self):
        head("# 准备测试ViewSet的post请求")
        head1("## 看看post调用的是create还是post")
        info("如果是post请求，调用的是create函数")
        client = Client()
        response = client.post(
            "/testapp/testfilter/?format=json",
            headers={"accept": "application/json"},
            json={
                "_type": "类型1"
            }
        )
        info(f"服务器返回的状态码: {response.status_code}")
        info(f"服务器返回的状态码: {response.content.decode('UTF-8')}")
