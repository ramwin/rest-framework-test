# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from . import serializers

# Create your views here.
log = logging.getLogger("default")


class MyLoginView(CreateAPIView):
    """这个接口既会登录设置cookie, 又会返回token"""
    serializer_class = serializers.AuthenticationSerializer

    def post(self, request, *args, **kwargs):
        log.info("用户{}登录了".format(request.user))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = {
            "token": Token.objects.get_or_create(user=request.user)[0].key
        }
        log.info(request.user)
        # 这里不能用Response, 因为会把数据
        return Response(result, status=201)
