#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 22:50
# @Author  : Evescn
# @Site    : 
# @File    : 多进程queue.py
# @Software: PyCharm

from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])

def f2(q):
    # print('from f2:',q.get())  # prints "[42, None, 'hello']"
    q.put([42, None, 'hello'])
    print('from f21:', q.get())  # prints "[42, None, 'hello']"

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print('from parent1:', q.get())  # prints "[42, None, 'hello']"
    p.join()

    p2 = Process(target=f2, args=(q,))
    p2.start()
    print('from parent2:',q.get())  # prints "[42, None, 'hello']"
    p2.join()