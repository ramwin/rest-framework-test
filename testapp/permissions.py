#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-16 15:36:37


import logging
from rest_framework.permissions import BasePermission


log = logging.getLogger('default')


class TestPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        # 注意，这个action只有在viewset里面才有，不可用于apiview
        log.info("校验{}权限".format(view.action))
        logging.info("校验{}权限".format(view.action))
        if view.action == "retrieve":
            return True
        return True
