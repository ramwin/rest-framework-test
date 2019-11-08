#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-04-08 10:59:59

from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from testapp import head, head1, list1, list2, info


head("# 准备测试用户认证模块1")
User = get_user_model()


class AuthTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='rightpassword')

    def test_user_modal(self):
        head1("## 准备测试用户model")
        list1("* 测试model的fields username")
        user = User.objects.create()
        info("直接创建用户成功")
        info("用户的username为空字符串")
        self.assertEqual(user.username, "")

    def test_auth_views(self):
        head1("## 准备测试使用auth的view进行登录")
        client = Client()
        response = client.post(
            "/api-auth/login/",
            data={"username": "username", "password": "rightpassword"},
            header={
                "content-type": "application/json; charset=utf-8"
            }
        )
        self.assertIsNotNone(response.cookies.get('sessionid'))
        response = client.get(
            "/testapp/movie/"
        )
        self.assertEqual(response.context['user'], self.user)
        response = client.get(
            "/api-auth/logout/",
        )
        self.assertFalse(response.context['user'].is_authenticated)
