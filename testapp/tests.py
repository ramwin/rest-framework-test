# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import json

from django.test import TestCase
from django.test import Client

from testapp.models import BasicModel
from testapp import models, serializers

# Create your tests here.
log = logging.getLogger('django')


class AnimalTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        pass

    def test_create_many_serializer(self):
        many_create_data = {
            "texts": json.dumps([
                {"text": "text"},
                {"text": "text"},
                {"text": "text"},
            ])
        }
        response = self.client.post("/testapp/manycreate/", data=many_create_data)
        log.info("response.data: {}".format(response.data))
        manyinstance = models.ManyModel.objects.get(id=response.data['id'])
        log.info(manyinstance.texts.all())
        log.info(BasicModel.objects.all())
        log.info(serializers.TestManyCreateSerializer(models.ManyModel.objects.first()).data)
