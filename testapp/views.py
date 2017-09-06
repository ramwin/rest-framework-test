# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from . import models, serializers

# Create your views here.


class BasicModelView(ListCreateAPIView):
    """
    get:
    返回Text列表

    post:
    创建Text
    """
    queryset = models.BasicModel.objects.all()
    serializer_class = serializers.BasicModelSerializer
    filter_fields = ['text']




class BasicModelDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.BasicModel.objects.all()
    serializer_class = serializers.BasicModelSerializer
    filter_fields = ['text']
