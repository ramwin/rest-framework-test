#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-10-10 15:54:46


import logging
from rest_framework import serializers
from django.contrib.auth import authenticate, login


log = logging.getLogger("default")


class AuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        fields = ["username", "password"]

    def validate(self, validated_data):
        log.info("准备校验密码")
        request = self.context["request"]
        user = authenticate(request=request, **validated_data)
        if user is None:
            raise serializers.ValidationError({"username": "用户名或者密码不正确"})
        log.info("准备login设置cookie")
        # 两个都可以
        # login(request._request, user)
        login(request, user)
        request.user = user
        log.info(validated_data)
        return validated_data
