# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


def myfunction():
    return ""


class User(AbstractUser):
    userid = models.CharField(default=myfunction, max_length=32)

    class Meta(AbstractUser.Meta):
        verbose_name_plural = "用户"
