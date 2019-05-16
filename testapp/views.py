# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import ipdb
import json
import tempfile

from django.http import FileResponse, HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView,
    ListAPIView,
)
from rest_framework.pagination import PageNumberPagination, CursorPagination
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from . import models, serializers, filters, paginations, permissions
from rest_framework.response import Response

# Create your views here.

log = logging.getLogger('django')


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
    http_method_names = ['post']

    def get_serializer(self, *args, **kwargs):
        # import ipdb
        # ipdb.set_trace()
        if 'data' in kwargs:
            data = kwargs['data']
            # data['text'] = 'new text'
        return super(BasicModelView, self).get_serializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        log.info(request.data)
        log.info(type(request.data))
        # ipdb.set_trace()
        return super(BasicModelView, self).post(request, *args, **kwargs)


class BasicModelDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.BasicModel.objects.all()
    serializer_class = serializers.BasicModelSerializer
    filter_fields = ['text']

    def finalize_response(self, request, response, *args, **kwargs):
        # import ipdb
        # ipdb.set_trace()
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
    filter_class = filters.TestFilterClass2


class ManyCreateView(CreateAPIView):
    serializer_class = serializers.TestManyCreateSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data["texts"] = json.loads(data["texts"])
        log.info(data)
        data = { 
            "texts": [
                {"text": "text"},
                {"text": "text"},
                {"text": "text"},
            ]
        }
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        log.info(self.serializer_class(serializer.instance).data)
        return Response(serializer.data)


class TestFilterViewSet(ModelViewSet):
    queryset = models.TestFilter.objects.all()
    serializer_class = serializers.TestFilterSerializer2
    filter_class = filters.TestFilterClass3

    def post(self, request, *args, **kwargs):
        log.info("调用TestFilterViewSet.post")
        return super(TestFilterViewSet, self).post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        log.info("调用TestFilterViewSet.create")
        log.info(f"当前动作{self.action}")
        return Response({"detail":"不能调用哦"}, status=409)
        response = super(TestFilterViewSet, self).create(request, *args, **kwargs)
        return response


class URLView(TemplateView):
    template_name = "testapp/测试模板.html"

    def get_template_names(self):
        if self.request.resolver_match.kwargs["scene"] == "admin":
            return ["testapp/测试模板_admin.html"]
        else:
            return [self.template_name]


class TestPathView(TemplateView):

    def get(self, request, *args, **kwargs):
        log.info("测试url路径")
        log.info(kwargs)
        return render(
            request, "testapp/测试模板.html",
            kwargs
        )


class TemplateTestView(TemplateView):
    template_name = "testapp/测试模板.html"


class TestViewSet(ModelViewSet):
    queryset = models.BasicModel.objects.all()
    serializer_class = serializers.BasicModelSerializer
    # filter_fields = ["text", "ordering"]
    # filterset_fields = ["text"]
    filter_class = filters.TestOrderFilter
    pagination_class = CursorPagination
    permission_classes = [permissions.TestPermission]
