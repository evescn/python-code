#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 20:15
# @Author  : Evescn
# @Site    : 
# @File    : sock_client3.py
# @Software: PyCharm

import socket
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)

while True:
    user_input = input("cmd$ ").strip()
    if len(user_input) == 0 : continue
    if user_input == 'q': break
    sk.send(bytes(user_input,'utf8'))
    #while True:
    #ack_msg = b"CMD_RESULT_SIZE|%s" %len(cmd_result)
    server_ack_msg = sk.recv(100)
    cmd_res_msg = str(server_ack_msg.decode()).split("|")
    while True:
        print("server responds:", server_ack_msg)
        print("cmd_res_msg:", cmd_res_msg[0])
        if cmd_res_msg[0] == "CMD_RESULT_SIZE":
            cmd_res_size = int(cmd_res_msg[1])
            sk.send(b"start")
            break
    res = ''
    received_size=0
    while received_size < cmd_res_size:
        server_reply = sk.recv(500)
        res += str(server_reply, 'utf8')
        received_size += len(server_reply)
    else:
            print(res)
            print("------ reve doene -------")

sk.close()

