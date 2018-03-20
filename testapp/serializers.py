#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-09-05 12:03:51


from django.core.validators import MaxValueValidator
from django.utils import timezone

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


class MyValidator(object):

    def __call__(self, value):
        print('calling validator')
        if value != 2:
            print("%s不是2呢" % value)
            raise serializers.ValidationError("不是2哦")


class MyField(serializers.RegexField):
    # validators = [MyValidator]
    regex = r'\d+'

    def __init__(self, **kwargs):
        super(MyField, self).__init__(self.regex, **kwargs)
        validator = MyValidator()
        self.validators.append(validator)

    def to_internal_value(self, data):
        print('calling to_internal_value')
        self.run_validators(data)
        print("转化数据")
        return 2


class MySerializer(serializers.Serializer):
    field = MyField()

    class Meta:
        model = models.MyModel
        fields = ['field']

    def save(self):
        pass


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FileModel
        fields = ["fil", 'integer']
        extra_kwargs = {
            'fil': {
                # 'use_url': False
            }
        }


class ManySerializer(serializers.ModelSerializer):
    texts = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = models.ManyModel
        fields = ["texts"]


class ManyDetailSerializer(serializers.ModelSerializer):
    texts = serializers.ListField(source="texts.text")

    class Meta:
        model = models.ManyModel
        fields = ["texts"]


class FileModelSerializer1(serializers.ModelSerializer):
    a = serializers.SerializerMethodField()

    def get_a(self, instance):
        return 'a1'

    class Meta:
        model = models.FileModel
        fields = ['fil', 'a']

class FileModelSerializer2(serializers.ModelSerializer):
    a = serializers.SerializerMethodField()

    class Meta:
        model = models.FileModel
        fields = ['integer', 'a']

    def get_a(self, instance):
        return 'a'


class FileModelSerializer3(FileModelSerializer2, FileModelSerializer1):
    class Meta(FileModelSerializer1.Meta):
        fields = list(set(FileModelSerializer1.Meta.fields + FileModelSerializer2.Meta.fields))


class ForeignKeySerializer(serializers.ModelSerializer):
    text = BasicModelSerializer(many=True, )

    class Meta:
        model = models.ForeignKeyModel
        fields = ['text', 'id']

    def create(self, validated_data):
        text = validated_data.pop('text')
        print(text[0])
        return super(ForeignKeySerializer, self).create(validated_data)


class PartialModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PartialModel
        fields = ["text1", "text2", "text3"]
        read_only_fields = ["text1"]


class TestNullSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestNullModel
        fields = ["can_null_blank", "can_null", "can_blank",
                  "can_default", "can"]


class TestHiddenField(serializers.Serializer):
    time1 = serializers.HiddenField(default=timezone.now)

    class Meta:
        fields = ["text"]


class TestAutoNowAddSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ["text", "time"]


class ForeignKey2Serializer(serializers.ModelSerializer):

    class Meta:
        model = models.ForeignKeyModel2


class TestRegexSerializer(serializers.Serializer):
    avatar = serializers.RegexField(regex="tmp-.*")

    class Meta:
        fields = ["avatar"]
