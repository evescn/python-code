#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 22:24
# @Author  : Evescn
# @Site    : 
# @File    : type-lx.py
# @Software: PyCharm

evescn  = type("evescn", (), {"test":123, "name": "evescn"})
print(type(evescn))
# print(evescn)

a = evescn()
print(a.__dict__)
print(a.test)
print(a.name)