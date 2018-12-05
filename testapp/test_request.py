#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-11-16 17:25:39


import ipdb

from django.test import TestCase
from django.test import Client

from testapp import head, head1, list1, list2, info


class RequestTestCase(TestCase):

    def test_request_data(self):
        head1("准备测试request.data")
        list1("* 测试request.data类型,是否可变")
        client = Client()
        response = client.post("/testapp/basicmodel/", {"text": "text"})
        # ipdb.set_trace()
