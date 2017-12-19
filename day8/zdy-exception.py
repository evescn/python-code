#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 22:48
# @Author  : Evescn
# @Site    : 
# @File    : zdy-exception.py
# @Software: PyCharm

class EveScnException(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


try:
    raise EveScnException('我的异常')
except EveScnException as e:
    print(e)