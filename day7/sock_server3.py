#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 20:10
# @Author  : Evescn
# @Site    : 
# @File    : sock_server3.py
# @Software: PyCharm

import socket
import subprocess
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print("server waiting...")
    conn,addr = sk.accept()
    while True:
        client_data = conn.recv(1024)
        if not client_data: break
        print("recv cmd:", str(client_data, 'utf8'))
        cmd = str(client_data, 'utf8').strip()
        cmd_call = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        cmd_result = cmd_call.stdout.read()
        if len(cmd_result) == 0:
            cmd_result = b'commond is not found'
        cmd_len = len(cmd_result)
        ack_msg = bytes("CMD_RESULT_SIZE|%s" %len(cmd_result), 'utf8')
        conn.send(ack_msg)
        conn.recv(10)
        conn.send(cmd_result)
    conn.close()
