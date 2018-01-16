#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 22:28
# @Author  : Evescn
# @Site    : 
# @File    : 多进程.py
# @Software: PyCharm

from multiprocessing import Process
import time


def f(name):
    time.sleep(2)
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p2 = Process(target=f, args=('bob',))
    p3 = Process(target=f, args=('bob',))
    p.start()
    p2.start()
    p3.start()
    p.join()