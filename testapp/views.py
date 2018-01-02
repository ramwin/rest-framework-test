# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ipdb

from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
)
from . import models, serializers
from rest_framework.response import Response

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

    def finalize_response(self, request, response, *args, **kwargs):
        import ipdb
        ipdb.set_trace()
        return super(BasicModelDetailView, self).finalize_response(request, response, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return Response({})


class FileView(ListCreateAPIView):
    queryset = models.FileModel.objects.all()
    serializer_class = serializers.FileSerializer
