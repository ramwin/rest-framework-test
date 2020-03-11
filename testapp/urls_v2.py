#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-01-09 09:16:46


from django.urls import path
from . import views


app_name = "testapp_v2"
urlpatterns = [
    path('testint/<slug:pk>/', views.TestPathView2.as_view(), name="testint"),
    path("not_exist_in_urls/", views.TestPathView.as_view()),
]
