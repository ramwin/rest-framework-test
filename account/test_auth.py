#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-10-10 15:57:49


from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from testapp import head, head1, list1, list2, info


head("# 准备测试用户认证模块2")
User = get_user_model()


class AuthTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username="用户名", password="密码")
        self.user2 = User.objects.create_user(username="用户2", password="密码")

    def test_auth_views(self):
        head1("## 准备测试使用auth的view进行登录")
        client = APIClient()
        response = client.post(
            "/account/login/",
            data={"username": "用户名", "password": "密码"},
            format="json",
        )
        self.assertEqual(
            Token.objects.get(key=response.json()["token"]).user,
            self.user1)
        self.assertIsNotNone(response.cookies.get('sessionid'))
        self.assertIsInstance(response.json()["token"], str)
        response = client.post(
            "/account/login/",
            data={"username": "用户2", "password": "密码"},
            format="json",
        )
        self.assertEqual(
            Token.objects.get(key=response.json()["token"]).user,
            self.user2)
