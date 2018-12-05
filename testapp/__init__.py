import sys

from django.core.management.base import OutputWrapper
from django.core.management.color import color_style


out = OutputWrapper(sys.stdout)
style = color_style()


def head(text):
    out.write(style.SQL_TABLE(text))

def head1(text):
    out.write(style.MIGRATE_HEADING(text))

def list1(text):
    out.write(style.SQL_FIELD(text))

def list2(text):
    out.write(style.SQL_COLTYPE(text))

def info(text):
    out.write(style.HTTP_INFO(text))
