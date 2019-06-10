#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-03-28 16:48:33


from django.test import Client
from django.test import TestCase

from rest_framework.test import APIClient

from testapp import head, head1, list1, list2, info
from testapp import models


head("# 准备测试viewset")
client = Client()
apiclient = APIClient()


class ViewSetFilter(TestCase):

    def test_viewset_post(self):
        head("# 准备测试ViewSet的post请求")
        head1("## 看看post调用的是create还是post")
        info("如果是post请求，调用的是create函数")
        response = client.post(
            "/testapp/testfilter/?format=json",
            headers={"accept": "application/json"},
            json={
                "_type": "类型1"
            }
        )
        info(f"服务器返回的状态码: {response.status_code}")
        info(f"服务器返回的状态码: {response.content.decode('UTF-8')}")

    def test_viewset_permission(self):
        head("# 准备测试ViewSet的permission")
        head1("## 看看detail的请求时候，permission里面有没有action")
        obj = models.BasicModel.objects.create(text="类型1")
        res = apiclient.get(
            "/testapp/modelviewset/{}/".format(obj.id), format="json")
        # import ipdb
        # ipdb.set_trace()
