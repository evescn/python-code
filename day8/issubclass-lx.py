#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 22:12
# @Author  : Evescn
# @Site    : 
# @File    : issubclass-lx.py
# @Software: PyCharm

class Foo(object):
    pass


class Bar(Foo):
    pass


print(issubclass(Bar, Foo))