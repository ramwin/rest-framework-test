#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-03-15 15:23:12


import ipdb

from django.test import TestCase, Client

from testapp import head, head1, list1, list2, info


head("# 准备测试template")


class TemplateTestCase(TestCase):

    def test_template(self):
        head1("\n## 测试模板")
        list1("* 测试不同的url,的参数的传递")
        client = Client()
        info("通过request.resolver_match.kwargs可以获取到url里面额外的参数")
        response = client.get("/testapp/url/")
        self.assertEqual(response.template_name, ["testapp/测试模板.html"])
        info("根据这个参数来判断要使用admin的template还是普通的template")
        response2 = client.get("/testapp/url2/")
        self.assertEqual(response2.template_name, ["testapp/测试模板_admin.html"])
