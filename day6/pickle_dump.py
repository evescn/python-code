#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 22:18
# @Author  : Evescn
# @Site    : 
# @File    : pickle_dump.py
# @Software: PyCharm
import shelve
import pickle

d = shelve.open('shelve_test')  # 打开一个文件


class Test(object):
    def __init__(self, n):
        self.n = n


t = Test(123)
t2 = Test(123334)

name = ["alex", "rain", "test"]
# d["test"] = name  # 持久化列表
# d["t1"] = t  # 持久化类
# d["t2"] = t2

f = open("pickle_test.pk1", "wb")
pickle.dump(name,f)
pickle.dump(t2,f)
pickle.dump(t,f)
f.close()

f1 = open("pickle_test.pk1", "rb")
a = pickle.load(f1)
print(a)    # dump进了第一次的数据

b = pickle.load(f1)
print(b.n)    # dump进了第二次数据

c = pickle.load(f1)
print(c.n)    #

f1.close()

