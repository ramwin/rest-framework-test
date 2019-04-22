#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-04-17 11:09:53

import datetime
import uuid
from django import template

register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def uuid_gen():
    return uuid.uuid4().hex


@register.filter(name='useruuid')
def useruuid(user):
    return uuid.uuid4().hex
