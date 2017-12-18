#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-12-12 11:35:01


from django.core.management.base import BaseCommand
from testapp.models import DateTimeModel
from testapp.filters import DateTimeFilter
import json


class Command(BaseCommand):

    def print_qs(self, queryset):
        self.stdout.write(self.style.SUCCESS(
            sorted(set(map(lambda x: x.time.isoformat(), queryset)))))

    def handle(self, *args, **kwargs):
        DateTimeModel.objects.get_or_create(
            time='2017-12-11T03:19:27.105918+00:00')
        DateTimeModel.objects.get_or_create(
            time='2017-12-12T03:19:05.483409+00:00')
        self.stdout.write(self.style.SUCCESS("当前有的时间"))
        self.print_qs(DateTimeModel.objects.all())
        param_list = [
            {},
            {'time': '2017-12-11T03:19:27.105918+00:00'},
            {'time__gt': '2016-12-11T02:19:27.105918+00:00'},
            {'time__gt': '2017-12-11 03:19:27'},
            {'time__gt': '2017-12-11 03:19:28'},
            {'time__gt': '2017-12-11 11:19:27'},
            {'time__gt': '2017-12-11 11:19:28'},
            {'time__gt': '2017-12-11T11:19:27+08:00'},
            {'time__gt': '2017-12-11T11:19:28+08:00'},
            {'time__gt': '2017-12-11T11:19:27+00:00'},
            {'time__gt': '2017-12-11T11:19:28+00:00'},
            {'time__gt': '2017-12-11T03:19:27+00:00'},
            {'time__gt': '2017-12-11T03:19:28+00:00'},
        ]
        for param in param_list:
            self.test_params(param)

    def test_params(self, params):
        self.stdout.write(self.style.HTTP_INFO("=====测试start====="))
        self.stdout.write(self.style.MIGRATE_HEADING("当前参数"))
        self.stdout.write(self.style.NOTICE(json.dumps(params)))
        self.print_qs(DateTimeFilter(params).qs)
        self.stdout.write(self.style.HTTP_INFO("=====测试 end ====="))
