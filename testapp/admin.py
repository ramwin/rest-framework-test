# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.FileModel)
admin.site.register(models.PartialModel)
admin.site.register(models.GetOrCreateModel)

class TestAdmin(admin.ModelAdmin):
    list_display = ["id", "img", "thumbnail"]

    def thumbnail(self, obj):
        from django.utils.html import format_html
        return format_html('<img src="{}" style="width: 130px; \
                            height: 100px"/>'.format(obj.img))

    thumbnail.short_description = 'thumbnail'

admin.site.register(models.TestAdminModel, TestAdmin)
