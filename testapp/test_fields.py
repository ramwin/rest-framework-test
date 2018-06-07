#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-05-21 17:07:05

import ipdb
import sys
import datetime
import pytz

from django.core.management.base import OutputWrapper
from django.core.management.color import color_style

from django.test import TestCase
from testapp.models import DateTimeModel
from testapp import models
from django.utils import timezone


out = OutputWrapper(sys.stdout)
style = color_style()


class FieldTestCase(TestCase):

    def setUp(self):
        out.write(style.MIGRATE_HEADING("准备测试Field"))
        pass

    def test_onetoone_field(self):
        text = models.BasicModel.objects.create(text="text")
        onetoone = models.TestOneToOneField.objects.create(text=text)
        text.delete()
        # CASCADE null=False|True, 此时可以用text.testonetoonefield 但是调用 text.testonetoonefield.refresh_from_db 就会报错
        out.write(style.HTTP_INFO("text已经删除"))
        out.write(style.HTTP_INFO(models.TestOneToOneField.objects.all()))
        # ipdb.set_trace()
