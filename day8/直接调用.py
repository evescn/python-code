#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 9:04
# @Author  : Evescn
# @Site    : 
# @File    : 直接调用.py
# @Software: PyCharm

import threading
import time


def sayhi(num):     # 定义每个线程要运行的函数
    print("running on number:%s" % num)

    time.sleep(3)


if __name__ == '__main__':
    t1 = threading.Thread(target=sayhi, args=(1,))  # 生成一个线程示例
    t2 = threading.Thread(target=sayhi, args=(2,))  # 生成另一个现场示例

    t1.start()
    t2.start()

    print(t1.getName())
    print(t2.getName())