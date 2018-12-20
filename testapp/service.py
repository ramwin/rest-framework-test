#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-12-20 17:16:40


import time
from django.views.decorators.cache import cache_control


@cache_control(max_age=60)
def slow_function(sleep=0):
    time.sleep(sleep)
    return sleep
