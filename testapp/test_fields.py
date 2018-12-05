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
from testapp.models import DateTimeModel, Student, Teacher
from testapp import models
from django.utils import timezone


out = OutputWrapper(sys.stdout)
style = color_style()


def head(text):
    out.write(style.SQL_TABLE(text))

def head1(text):
    out.write(style.MIGRATE_HEADING(text))

def list1(text):
    out.write(style.SQL_FIELD(text))

def list2(text):
    out.write(style.SQL_COLTYPE(text))

def info(text):
    out.write(style.HTTP_INFO(text))



class FieldTestCase(TestCase):

    def setUp(self):
        head("# 准备测试Field")
        pass

    def test_onetoone_field(self):
        head1("## 测试OneToOneField")
        text = models.BasicModel.objects.create(text="text")
        onetoone = models.TestOneToOneField.objects.create(text=text)
        text.delete()
        # CASCADE null=False|True, 此时可以用text.testonetoonefield 但是调用 text.testonetoonefield.refresh_from_db 就会报错
        out.write(style.HTTP_INFO("text已经删除"))
        out.write(style.HTTP_INFO(models.TestOneToOneField.objects.all()))

    def test_manytomany_field(self):
        head1("\n## 测试ManyToManyField")
        list1("* 如果symmetrical=True默认")
        student = Student.objects.create(name="George")
        student2 = Student.objects.create(name="Li Lei")
        student3 = Student.objects.create(name="Han Mei")
        student2.friends.add(student)
        student2.friends.add(student3)
        student3.friends.add(student2)
        print("student2的好友有:", end=" ")
        print(student2.friends.all())
        print("认为我是好友的有(只能是一样的):", end=" ")
        # print(student2.student_set.all()) 这个会报错
        print(student2.friends.all())
        list1("* 如果symmetrical=False")
        teacher = Teacher.objects.create(name="王主任")
        teacher2 = Teacher.objects.create(name="小李主任")
        teacher3 = Teacher.objects.create(name="小红主任")
        teacher2.teachers.add(teacher)
        teacher2.teachers.add(teacher3)
        teacher3.teachers.add(teacher)
        print("给teacher3指导过的有:", end=" ")
        print(teacher3.teachers.all())
        print("teacher3指导过的人有:", end=" ")
        # import ipdb
        # ipdb.set_trace()
        print(teacher3.teacher_set.all())
        head1("ManyToManyField测试完毕")
