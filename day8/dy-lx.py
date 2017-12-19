#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 22:52
# @Author  : Evescn
# @Site    : 
# @File    : dy-lx.py
# @Software: PyCharm

class EveScnException(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


a = 1
try:
    assert a == 1
    # raise EveScnException('我的异常')
except EveScnException as e:
    print(e)
else:
    print("hahaha")
finally:
    print("no matter right or wrong, run this anyway!")