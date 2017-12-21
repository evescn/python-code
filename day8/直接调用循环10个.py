#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 9:28
# @Author  : Evescn
# @Site    : 
# @File    : 直接调用循环10个.py
# @Software: PyCharm

import threading
import time


def sayhi(num):
    print("Running On Number:%s" % num)
    # print("running on number:%s" % num)
    time.sleep(3)


if __name__ == '__main__':
    a = []
    for i in range(10):
        t = threading.Thread(target=sayhi, args=(i,))
        t.start()
        a.append(t)

    for i in a:
        i.join()

    print("----main----")
