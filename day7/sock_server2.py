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
    client_data = conn.recv(1024)
    print(str(client_data,'utf8'))
    conn.sendall(bytes('不要回答，不要回答，不要回答','utf8'))
    while True:
        try:
            client_data = conn.recv(1024)
            print(str(client_data, 'utf8'))
        except Exception:
            print("client closed , break")
            break
        # server_response = input(">>:".strip())
        # conn.sendall(bytes(server_response, 'utf8'))
        if not client_data: break
        conn.send(client_data)
    conn.close()