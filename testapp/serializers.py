#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-09-05 12:03:51


from rest_framework import serializers
from . import models


class BasicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasicModel
        fields = "__all__"

    def to_representation(self, instance):
        # import ipdb
        # ipdb.set_trace()
        # if self.context['request'].user.level <= instance.userl.level:
        #     self.fields.pop('mobile_phone')
        return super(BasicModelSerializer, self).to_representation(instance)
