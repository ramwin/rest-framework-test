#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-03-11 17:40:20

class DEFAULTROUTER:
    def db_for_read(self, model, **hints):
        if not getattr(model, "Params", None):
            return "default"
        return getattr(model.Params, "db", "default")

    def db_for_write(self, model, **hints):
        if not getattr(model, "Params", None):
            return "default"
        return getattr(model.Params, "db", "default")

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == "database2" and app_label == "testapp":
            return db == "database2"
        else:
            return db == "default"

        # 这样不可行，因为migrate还没有执行，contenttype还没有生成
        ct = ContentType.objects.get(model=model_name, app_label=app_label)
        model = ct.model_class()
        if not getattr(model, "Params", None):
            return db == "default"
        return getattr(model.Params, "db", "default") == db
