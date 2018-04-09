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


class ManyDetail2Serializer(serializers.ModelSerializer):
    class MyBasicModelSerializer(BasicModelSerializer):
        def to_representation(self, instance):
            import ipdb
            ipdb.set_trace()

    # 这个不行，还是一条一跳的
    # texts = MyBasicModelSerializer(many=True)
    class MyListSerializer(serializers.ListSerializer):
        pass
    # 下面这个也失败，child无法放序列化类
    # texts = MyListSerializer(child=BasicModelSerializer)

    class Meta:
        model = models.ManyModel
        fields = ["texts", "id"]


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
        fields = "__all__"


class TestRegexSerializer(serializers.Serializer):
    avatar = serializers.RegexField(regex="tmp-.*")

    class Meta:
        fields = ["avatar"]


class TestMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestMethodModel
        # fields = "__all__"  # 不会有get_num
        fields = ["text", "get_num", "id"]


class TestMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BasicModel
        fields = ["id", "text",]
        write_only_fields = ["text"]


class TestValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ValidateModel
        fields = ["status"]

    def validate_status(self, value):
        # 这个只有默认的validate通过了，才会调用
        # 调用的时候，value已经是转化过了的
        print("调用了validate_status方法")
        print(value)
        print(type(value))
        return value


class TestToRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasicModel
        fields = ["text", "id"]

    def to_representation(self, instance):
        print("调用to_representation")  # 如果是直接is_valid()后调用 .data, 就会出现这个不是instance而是OrderedDict的情况
        print(instance)
        print(type(instance))
        return super(TestToRepresentationSerializer, self).to_representation(
            instance)
