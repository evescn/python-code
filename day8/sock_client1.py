#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 21:50
# @Author  : Evescn
# @Site    : 
# @File    : sock_client1.py
# @Software: PyCharm

import socket
ip_port = ('127.0.0.1',50007)

sk = socket.socket()
sk.connect(ip_port)

while True:
    user_input = input(">>:").strip()
    sk.send(bytes(user_input,'utf8'))
    server_reply = sk.recv(1024)
    print("Server Reply:", str(server_reply, 'utf8'))


sk.close()