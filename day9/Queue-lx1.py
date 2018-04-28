#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 10:01
# @Author  : Evescn
# @Site    : 
# @File    : Queue-lx1.py
# @Software: PyCharm

import queue
class Foo(object):
    def __init__(self,num):
        self.num = num


q = queue.Queue(maxsize=3)
q.put([1,2,3,])
q.put(Foo(1))
q.put(1)
# q.put(2,timeout=3)
print(q.qsize())
print(q.full())
# q.get(timeout=3)
# q.get_nowait()
data1 = q.get_nowait()
data = q.get_nowait()
print(data)
print(type(data))
