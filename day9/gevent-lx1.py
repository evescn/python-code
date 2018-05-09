#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 15:44
# @Author  : Evescn
# @Site    : 
# @File    : gevent-lx1.py
# @Software: PyCharm

import gevent, threading

def task(pid):
    """
    Some non-deterministic task
    :param pid:
    :return:
    """
    gevent.sleep(0.5)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1, 10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()