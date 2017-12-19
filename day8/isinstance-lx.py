#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 22:14
# @Author  : Evescn
# @Site    : 
# @File    : isinstance-lx.py
# @Software: PyCharm

class Foo(object):
    pass


obj = Foo()

print(isinstance(obj, Foo))

a = [2, 3, 5]

if type(a) is list: print(a)

if isinstance(a, list): print(a)