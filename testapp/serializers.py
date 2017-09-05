#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-09-05 12:03:51


from rest_framework import serializers
from . import models


class BasicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasicModel
        fields = "__all__"
