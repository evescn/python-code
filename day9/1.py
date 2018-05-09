#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 13:52
# @Author  : Evescn
# @Site    : 
# @File    : 1.py
# @Software: PyCharm

import select
import socket
import sys
import queue

server = socket.socket()
server.setblocking(0)

server_addr = ('localhost', 10001)

print('starting up on %s port %s' % server_addr)
server.bind(server_addr)

server.listen(5)

inputs = [server, ]
outputs = []

message_queues = {}

while True:
    print("waiting for next event...")

    readable, writeable, exeptional = select.select(inputs, outputs, inputs)

    for s in readable:

        if s is server:
            conn, client_addr = s.accept()
            print("new connection from", client_addr)
            conn.setblocking(0)
            inputs.append(conn)

            message_queues[conn] = queue.Queue()
            print(message_queues)

        else:
            data = s.recv(1024)
            if data:
                print("收到来自[%s]的数据：" % s.getpeername()[0], data)
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
                    print(outputs)

            else:
                print("客户端断开了", s)

                if s in outputs:
                    print(outputs)
                    outputs.remove(s)
                    print(outputs)
                inputs.remove(s)

    for s in writeable:
        try:
            next_msg = message_queues[s].get_nowait()

        except queue.Empty:
            print("client [%s]" %s.getpeername()[0], "queue is empty..")
            outputs.remove(s)

        else:
            print("sending msg to [%s]" %s.getpeername()[0], next_msg)
            s.send(next_msg.upper())

    for s in exeptional:
        print("handling exception for ", s.getpeername())
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        del message_queues[s]

