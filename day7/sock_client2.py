#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 23:15
# @Author  : Evescn
# @Site    : 
# @File    : sock_client.py
# @Software: PyCharm

import socket
ip_port = ('127.0.0.1',9998)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall(bytes('请求占领地球','utf8'))

server_reply = sk.recv(1024)
# print(server_reply)
print(str(server_reply,'utf8'))

while True:
    user_input = input(">>:").strip()
    sk.send(bytes(user_input,'utf8'))
    server_reply = sk.recv(1024)
    print(str(server_reply, 'utf8'))

sk.close()
