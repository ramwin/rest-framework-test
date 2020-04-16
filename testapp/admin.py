# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# from import_export.admin import ImportExportMixin
from import_export import resources
from . import models

# Register your models here.
admin.site.register(models.FileModel)
admin.site.register(models.PartialModel)
admin.site.register(models.GetOrCreateModel)


@admin.register(models.TestAdminModel)
class TestAdmin(admin.ModelAdmin):
    list_display = ["id", "img", "thumbnail", "avatar"]

    def thumbnail(self, obj):
        from django.utils.html import format_html
        return format_html('<img src="{}" style="width: 130px; \
                            height: 100px"/>'.format(obj.img))

    thumbnail.short_description = 'thumbnail'
    readonly_fields = ["img", "avatar", "thumbnail"]
    # fields = ["id", "thumbnail"]


# admin.site.register(models.TestAdminModel, TestAdmin)
admin.site.site_header = 'site_header'


@admin.register(models.TestFilterModel)
class FilterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestDecimalModel)
class TestDecimalAdmin(admin.ModelAdmin):
    list_display = ["id", "deci"]
    pass


admin.site.register(models.MyModel)
admin.site.register(models.TestFilterThrough)
admin.site.register(models.TestNullModel)


@admin.register(models.TestAdminPermissionModel)
class AdminPermissionAdmin(admin.ModelAdmin):
    pass


class ImportModelResource(resources.ModelResource):
    import_id_fields = ["id"]

    class Meta:
        model = models.ImportModel
        fields = ("text", "id")


class ImportModelAdmin(ImportExportModelAdmin):
    resource_class = ImportModelResource
    list_display = ("text", "id")


admin.site.register(models.ImportModel, ImportModelAdmin)
