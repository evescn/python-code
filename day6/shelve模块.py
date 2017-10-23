#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 15:58
# @Author  : Evescn
# @Site    : 
# @File    : shelve模块.py
# @Software: PyCharm

import shelve

d = shelve.open("shelve_test")  # 打开一个文件


class Test(object):
    def __init__(self, n):
        self.n = n


t = Test(123)
t2 = Test(123334)

name = ["evescn", "gmkk", "hlr"]
d["test"] = name  # 持久化列表
d["t1"] = t  # 持久化类
d["t2"] = t2

d.close()

a = shelve.open("shelve_test")   # 文件名称

# print(dir(a))
print(a.get("test"))

b = a.get("t1")
c = a.get("t2")

print(a.get("t2"))
print(b.n)
print(c.n)