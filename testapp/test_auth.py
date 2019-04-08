#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-04-08 10:59:59

from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from testapp import head, head1, list1, list2, info


head("# 准备测试用户认证模块")
User = get_user_model()


class AuthTestCase(TestCase):

    def test_user_modal(self):
        head1("## 准备测试用户model")
        list1("* 测试model的fields username")
        user = User.objects.create()
        info("直接创建用户成功")
        info("用户的username为空字符串")
        self.assertEqual(user.username, "")
