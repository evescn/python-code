#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 23:10
# @Author  : Evescn
# @Site    : 
# @File    : sock_server.py
# @Software: PyCharm

import socket

ip_port = ('127.0.0.1',9998)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print("server waiting...")
    conn,addr = sk.accept()
    # conn.recv(1024)
    client_data = conn.recv(1024)
    # print(client_data)
    print(str(client_data,'utf8'))
    conn.sendall(bytes('不要回答，不要回答，不要回答','utf8'))
    conn.close()