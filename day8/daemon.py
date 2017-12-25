#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 21:05
# @Author  : Evescn
# @Site    : 
# @File    : daemon.py
# @Software: PyCharm

import time
import threading


def run(n):
    print('[%s]------running------\n' % n)
    time.sleep(2)
    print('--done--')


def main():
    for i in range(5):
        t = threading.Thread(target=run, args=[i,])
        t.start()
        # t.join(1)
        print('starting thread', t.getName())


m = threading.Thread(target=main, args=[])
m.setDaemon(True) # 将main线程设置为Daemon线程,它做为程序主线程的守护线程,当主线程退出时,m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务
m.start()
# m.join()
m.join(timeout=3)
print("---main thread done----")