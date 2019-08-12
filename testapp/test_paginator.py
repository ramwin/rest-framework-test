#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-07-26 16:23:06


from django.test import Client
from django.test import TestCase

from rest_framework.test import APIClient

from testapp import head, head1, list1, list2, info
from testapp import models


head("# 准备测试paginator")
client = Client()
apiclient = APIClient()


class PaginatorTest(TestCase):

    def test_paginator(self):
        head1("## 准备测试paginator的函数")
        res = apiclient.get(
            "/testapp/paginator/", format="json")
