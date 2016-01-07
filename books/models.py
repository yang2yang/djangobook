#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Publisher(models.Model):  # 都是继承了这个父类，之后的工作就是定义几个类变量，其他的其实什么都不用管，只需要熟悉这中接口就行了
    name = models.CharField(max_length=30)  # 标准的字符串的字段
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)  # 这句话要好好理解，多对多的关系，在Book中并没有这个authors字段，而是又创建了另外一个表
    publisher = models.ForeignKey(Publisher)  # 如何定义一个外键
    publication_date = models.DateField()  # 另外每一张表都有一个id作为主键，都是自增的

    def __str__(self):
        return self.title
