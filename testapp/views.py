# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ipdb
import tempfile

from django.http import FileResponse, HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView,
    ListAPIView,
)
from rest_framework.views import APIView
from . import models, serializers, filters
from rest_framework.response import Response

# Create your views here.


class BasicModelView(APIView):
    """
    get:
    返回Text列表

    post:
    创建Text
    """
    queryset = models.BasicModel.objects.all()
    # serializer_class = serializers.BasicModelSerializer
    filter_fields = ['text']
    http_method_names = ['post']

    def post(self, request):
        return Response('ew')


class BasicModelDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.BasicModel.objects.all()
    serializer_class = serializers.BasicModelSerializer
    filter_fields = ['text']

    def finalize_response(self, request, response, *args, **kwargs):
        import ipdb
        ipdb.set_trace()
        response = super(BasicModelDetailView, self).finalize_response(request, response, *args, **kwargs)
        return response

    def destroy(self, request, *args, **kwargs):
        return Response({})


class FileView(ListCreateAPIView):
    queryset = models.FileModel.objects.all()
    serializer_class = serializers.FileSerializer


class PartialModelPatchView(RetrieveUpdateDestroyAPIView):
    queryset = models.PartialModel.objects.all()
    serializer_class = serializers.PartialModelSerializer

    def get_serializer(self, *args, **kwargs):
        if 'partial' in kwargs:
            kwargs.pop('partial')
        print(kwargs)
        return self.serializer_class(*args, **kwargs)


class FileReturnView(APIView):

    def get(self, request, *args, **kwargs):
        if request._request.path.endswith("download/"):
            return render(request, "testapp/返回文件.html", {})
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix="csv")
        for i in range(1000):
            temp_file.write("hello\n")
        # return FileResponse(temp_file)

        # 使用straming会报错
        return StreamingHttpResponse("we", content_type="text/csv")

        # 直接返回文档和数据，但是这样名字是根据后缀名来的，不是根据下面的filename来的
        print("直接返回文档")
        response = HttpResponse(
            "ok", content_type="text/csv")
        response["Content-Disposition"] = "attachment:filename=\"{}\"".format(
            "test.csv"
        )
        return response


class TestFilterView(ListCreateAPIView):

    queryset = models.TestFilterModel.objects.all()
    serializer_class = serializers.TestFilterSerializer
    # filter_fields = ["status", "text"]
    filter_class = filters.TestFilterClass
