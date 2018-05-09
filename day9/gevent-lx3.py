#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 11:56
# @Author  : Evescn
# @Site    : 
# @File    : gevent-lx3.py
# @Software: PyCharm

import gevent
import socket


def func1():
    print('\033[31;1m李闯在跟海涛搞...\033[0m')
    gevent.sleep(2)
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


def func2():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
    gevent.sleep(1)
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')

def func3():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
    gevent.sleep(1)
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
])