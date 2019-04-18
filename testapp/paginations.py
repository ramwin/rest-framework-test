#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-04-18 11:56:40

from rest_framework import pagination


class PaginationClass(pagination.PageNumberPagination):
    page_size=10
    ordering = "-id"
