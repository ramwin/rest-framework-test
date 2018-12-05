from django.test import TestCase

# Create your tests here.


from datetime import date
import logging
import sys

from .models import Book, Author, Publisher, Store

from django.core.management.base import OutputWrapper
from django.core.management.color import color_style
from django.db.models import (
    Avg, Max, Count,
    Q,
    FloatField
)
from django.utils import timezone


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


def warning(text):
    out.write(style.WARNING(text))


class MyBookAppTestCase(TestCase):

    def setUp(self):
        author_wx = Author.objects.create(name="王祥", age=28)
        author_lcx = Author.objects.create(name="刘慈欣", age=55)
        publisher_sjtu = Publisher.objects.create(name="上海交通大学出版社")
        publisher_science = Publisher.objects.create(name="科幻世界")
        book_resume = Book.objects.create(
            name="我的传记", pages=12, price=18.8, rating=10,
            publisher=publisher_sjtu,
            pubdate=timezone.datetime(2018,1,1)
        )
        book_resume.authors = [author_wx]
        book_resume.save()

        book_santi = Book.objects.create(
            name="三体I - 地球往事", pages=1000, price=23.0, rating=1,
            publisher=publisher_science,
            pubdate=date(2008,1,1))
        book_santi.authors = [author_lcx]
        book_santi.save()

        book_santi_II = Book.objects.create(
            name="三体II - 黑暗森林", pages=470, price=43.0, rating=2,
            publisher=publisher_science,
            pubdate=date(2008,5,1))
        book_santi_II.authors = [author_lcx]
        book_santi_II.save()


    def test_aggregation(self):
        info("当前作者人数: {}".format(Author.objects.count()))
        info("作者的平均年龄: {}".format(
            Author.objects.all().aggregate(Avg('age'))))
        info("当前最贵的书的价格: {}".format(
            Book.objects.all().aggregate(Max('price'))))
        info("最贵的书比平均价格高: {}".format(
            Book.objects.aggregate(
                price_diff=Max('price', output_field=FloatField()) - Avg('price')
            )
        ))
        pubs = Publisher.objects.annotate(num_books=Count('book'))
        info("出版社<{}>出版的书籍数量 {}".format(
            pubs[0],
            pubs[0].num_books
        ))
        above_5 = Count('book', filter=Q(book__rating__gt=5))
        below_5 = Count('book', filter=Q(book__rating__lte=5))
        pubs = Publisher.objects.annotate(below_5=below_5).annotate(above_5=above_5)
        warning("2版本才开始支持filter这个参数, 1.11不能使用, 得到的数据和预想的不一样")
        info("出版社<{}> `rate > 5` 的书籍数量 {}".format(
            pubs[0],
            pubs[0].above_5,
        ))
        info("出版社<{}> `rate < 5` 的书籍数量 {}".format(
            pubs[0],
            pubs[0].below_5,
        ))
        pubs = Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')[:5]
        info("出版书籍最多的出版社 {}".format(pubs[0]))
        info("出版社<{}>出版的书籍数量: {}".format(
            pubs[0],
            pubs[0].num_books,
        ))
