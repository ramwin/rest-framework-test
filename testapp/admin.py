# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.FileModel)
admin.site.register(models.PartialModel)
admin.site.register(models.GetOrCreateModel)
