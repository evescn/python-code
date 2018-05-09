#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 11:58
# @Author  : Evescn
# @Site    : 
# @File    : greenlet-lx1.py
# @Software: PyCharm

from greenlet import greenlet
# import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()