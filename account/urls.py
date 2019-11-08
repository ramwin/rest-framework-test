#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-10-10 15:59:43


from django.urls import path
from . import views


app_name = "account"
urlpatterns = [
    path("login/", views.MyLoginView.as_view(), name="login"),
]
