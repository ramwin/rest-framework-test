#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-12-12 11:30:03


from . import models
import django_filters


class DateTimeFilter(django_filters.rest_framework.FilterSet):
    time__gt = django_filters.IsoDateTimeFilter(
        name="time", lookup_expr="gt")

    class Meta:
        model = models.DateTimeModel
        fields = ["time", "time__gt"]


class TestFilterClass(django_filters.rest_framework.FilterSet):

    class Meta:
        model = models.TestFilterModel
        fields = ["status", "text", "id", "content", "many", "many2"]


class TestFilterClass2(django_filters.rest_framework.FilterSet):
    many3 = django_filters.ModelChoiceFilter(name="many2", help_text="过滤many2", queryset=models.GetOrCreateModel.objects.all())

    class Meta:
        model = models.TestFilterModel
        fields = ["status", "text", "id", "content", "many", "many2", "many3"]


class TestMethodFilter(django_filters.rest_framework.FilterSet):
    _bool = django_filters.BooleanFilter(method="filter_bool")

    def filter_bool(self, queryset, name, value):
        print("name: {}".format(name))
        print("value: {}".format(value))
        return queryset

    class Meta:
        model = models.TestFilterModel2
        fields = ["_bool"]


class TestFilterClass3(django_filters.rest_framework.FilterSet):
    _type = django_filters.MultipleChoiceFilter(
        choices=models.TestFilter.TYPE_CHOICE
    )
    basic_model = django_filters.ModelMultipleChoiceFilter(
        queryset=models.BasicModel.objects.all(),
        distinct=True
    )

    class Meta:
        model = models.TestFilter
        fields = ["_type", "basic_model"]
