#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 11:17
# @Author  : evescn
# @Site    : 
# @File    : dg.py
# @Software: PyCharm


def func(arg1, arg2):
    # for i in range(10):
    if arg1 == 0:
        print(arg1)
        print(arg2)
    arg3 = arg1 + arg2
    if arg3 < 1000:
        print(arg3)
        func(arg2, arg3)
    else:
        return


func(0, 1)