#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 22:09
# @Author  : Evescn
# @Site    : 
# @File    : 信号量.py
# @Software: PyCharm

import threading,time


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s\n" %n)
    semaphore.release()


if __name__ == '__main__':
    num = 0
    semaphore = threading.BoundedSemaphore(3)
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()

while threading.active_count() != 1:
    # print("Now thread is num:", threading.active_count())
    pass
else:
    print("----all thread done----")
    print(num)