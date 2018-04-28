#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 10:13
# @Author  : Evescn
# @Site    : 
# @File    : Queue-lx3.py
# @Software: PyCharm

import queue
class Foo(object):
    def __init__(self,num):
        self.num = num


q = queue.PriorityQueue(maxsize=3)
q.put((10,[1,2,3,]))
q.put((5,Foo(1)))
q.put((3,1))
# q.put(2,timeout=3)
print(q.qsize())
print(q.full())
# q.get(timeout=3)
# q.get_nowait()
# data1 = q.get_nowait()
data = q.get_nowait()
print(data)
data = q.get_nowait()
print(data)
data = q.get_nowait()
print(data)
