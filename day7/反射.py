#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 22:58
# @Author  : Evescn
# @Site    : 
# @File    : 反射.py
# @Software: PyCharm

import sys

class WebServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        print("Server is starting...")

    def stop(self):
        print("Server is stopping...")

    def restart(self):
        self.stop()
        self.start()
        # print("Server is starting...")

def test_run(ins, name):
    print("running...", name, ins.host)

if __name__ == "__main__":
    # print(sys.argv[1])
    server = WebServer("localhost", 8080)
    server2 = WebServer("localhost", 8080)
    if hasattr(server, "start"):   # 判断有没有
        func  = getattr(server, "start")  # 获取server.start 方法的内存地址
        func() # server.start()

    # setattr(server, "run",test_run)  # 给实例绑定了一个方法
    # server.run(server, "gmkk")
    # server2.run(server, "gmkk")


    # delattr(server, 'start')   # 删除只能删除自己的，不能删除类的方法
    # delattr(server, 'host')   # 删除只能删除自己的，不能删除类的方法
    # print(server.host)

    delattr(WebServer, 'start')   # 删除只能删除自己的，不能删除类的方法
    print(server.restart())




    '''cmd_dic = {
        'start':server.start,
        'stop':server.stop,
        'restart':server.restart,
    }

    if sys.argv[1] in cmd_dic:
        cmd_dic[sys.argv[1]]()
    '''
