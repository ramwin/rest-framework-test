#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-12-12 11:30:03


from . import models
import django_filters


class DateTimeFilter(django_filters.rest_framework.FilterSet):
    time__gt = django_filters.IsoDateTimeFilter(name="time", lookup_expr="gt")
    class Meta:
        model = models.DateTimeModel
        fields = ["time", "time__gt"]
