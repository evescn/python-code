#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 14:17
# @Author  : Evescn
# @Site    : 
# @File    : 2.py
# @Software: PyCharm

import socket
import sys

messages = [ b'This is the message. ',
             b'It will be sent ',
             b'in parts.',
             ]
server_add = ('localhost', 10001)

socks = [
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
]

print('connecting to %s port %s' % server_add)
for s in socks:
    s.connect(server_add)

for messages in messages:

    for s in socks:
        print('%s: sending "%s"' %(s.getsockname(), messages))
        s.send(messages)

    for s in socks:
        data = s.recv(1024)
        print('%s: received "%s"' %(s.getsockname(), data))
        if not data:
            print(sys.stderr, 'closing socket', s.getsockname())
