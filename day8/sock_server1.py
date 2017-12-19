#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 21:45
# @Author  : Evescn
# @Site    : 
# @File    : sock_server1.py
# @Software: PyCharm

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("New Conn:", self.client_address)
        while True:
            data = self.request.recv(1024)
            if not data: break
            print("Client Says:", data.decode())
            self.request.send(data)


if __name__ == '__main__':
    HOST, PORT = "localhost", 50007

    # 吧刚才写的类当作一个参数传给ThreadingTCPServer这个类，下面的代码就创建了一个多现场socket server
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    # 启动这个server，这个server会一直运行，除非按ctrl-C停止
    server.serve_forever()