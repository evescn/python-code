#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 9:22
# @Author  : Evescn
# @Site    : 
# @File    : 继承式调用.py
# @Software: PyCharm

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("running on number:%s" % self.num)
        time.sleep(3)


if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()