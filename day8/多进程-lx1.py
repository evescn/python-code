#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 22:30
# @Author  : Evescn
# @Site    : 
# @File    : 多进程-lx1.py
# @Software: PyCharm

from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("\n\n")


def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)


if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = Process(target=info, args=('bob',))
    p.start()
    p.join()