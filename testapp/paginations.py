#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-04-18 11:56:40

import logging
from rest_framework import pagination
from collections import OrderedDict
from rest_framework.response import Response


log = logging.getLogger("django")


class PaginationClass(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        log.info("调用get_paginated_response")
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
