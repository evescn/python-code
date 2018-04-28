#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 10:56
# @Author  : Evescn
# @Site    : 
# @File    : q_task_done.py
# @Software: PyCharm

import threading, queue, time, random

def producer(name):
    count = 1
    # time.sleep(random.randint(1,5))
    while True:
        time.sleep(random.random())
        if q.qsize() < 2:
            print("[%s] 制作的包子 [%s]" %(name, count))
            q.put(count)
            count += 1
            q.join()
            print("[%s] 制作的所以的包子被领取了" %name )

def consumer(name):
    while True:
        print("[%s] 吃了第 [%s] 个包子" %(name, q.get()))
        time.sleep(1)
        q.task_done()

q = queue.Queue()

c1 = threading.Thread(target=consumer, args=["c1",])
c2 = threading.Thread(target=consumer, args=["c2",])
# c3 = threading.Thread(target=consumer, args=["c3",])

p1 = threading.Thread(target=producer, args=["p1",])
p2 = threading.Thread(target=producer, args=["p2",])
p3 = threading.Thread(target=producer, args=["p3",])

c1.start()
c2.start()
# c3.start()

p1.start()
p2.start()
p3.start()