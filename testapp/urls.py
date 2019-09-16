#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-09-05 12:01:43


from django.conf.urls import url
from django.urls import path
from . import views
from rest_framework import routers


app_name = "testapp"
router = routers.SimpleRouter()
router.register(r'testfilter', views.TestFilterViewSet)
router.register(r'modelviewset', views.TestViewSet)
router.register(r'log', views.TestLogViewSet)
router.register(r'paginator', views.TestPaginatorViewSet)

urlpatterns = router.urls + [
    url('^basicmodel/$', views.BasicModelView.as_view()),
    url('^basicmodel/(?P<pk>\d+)/$', views.BasicModelDetailView.as_view()),
    url(r'^file/$', views.FileView.as_view(), name="file"),
    url('^partialmodel/(?P<pk>\d+)/$', views.PartialModelPatchView.as_view()),
    url(r'^download/$', views.FileReturnView.as_view()),
    url(r'^download/123/$', views.FileReturnView.as_view()),
    url(r'^download/.*$', views.FileReturnView.as_view()),
    url(r'^testfilter/', views.TestFilterView.as_view()),
    url(r'^manycreate/', views.ManyCreateView.as_view()),
    url(r'^url/', views.URLView.as_view(),
        {"scene": "normal"}, name="url"),
    url(r'^url2/', views.URLView.as_view(),
        {"scene": "admin"}, name="url"),
    path('testint/<int:pk>/', views.TestPathView.as_view(), name="testint"),
    path('template/', views.TemplateTestView.as_view(), name="template"),
    path('movie/', views.MovieView.as_view(), name="movie"),
    path('movie.mp4', views.Mp4View.as_view(), name="mp4"),
]
