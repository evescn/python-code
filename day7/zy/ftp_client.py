#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 13:50
# @Author  : Evescn
# @Site    : 
# @File    : ftp_client.py
# @Software: PyCharm

import socket
import commons


ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(ip_port)

while True:
    username, password = commons.showinfo('login')
    sk.send(bytes("login", 'utf8'))
    # sk.send(bytes(user_input, 'utf8'))
    a1 = sk.recv(1024)
    # print("a1:", a1)
    sk.send(bytes(username, 'utf8'))
    a2 = sk.recv(1024)
    # print("a2:", a2)
    sk.send(bytes(password, 'utf8'))

    server_msg = sk.recv(1024)
    print("server_msg:", server_msg)
    print(type(server_msg.decode()))
    server_msg = str(server_msg, 'utf8')
    print(type(server_msg))
    if server_msg == '0':
        # 登录成功
        while True:
            cmd_result = commons.showinfo('show')
            print("cmd_result:", cmd_result)
            if cmd_result == 'ls' or cmd_result == 'cd' or cmd_result == 'dir':
                sk.send(bytes(cmd_result, 'utf8'))
                print("cmd_result:", cmd_result)
                server_ack_msg = sk.recv(100)
                print("server_ack_msg:", server_ack_msg)
                cmd_res_msg = str(server_ack_msg.decode()).split("|")
                while True:
                    # print("server responds:", server_ack_msg)
                    print("cmd_res_msg:", cmd_res_msg[0])
                    if cmd_res_msg[0] == "CMD_RESULT_SIZE":
                        cmd_res_size = int(cmd_res_msg[1])
                        sk.send(b"start")
                        break
                res = ''
                received_size = 0
                while received_size < cmd_res_size:
                    server_reply = sk.recv(4096)
                    print("server_reply：", server_reply)
                    # print(type(server_reply.decode('utf-8')))
                    # print("server_reply", str(server_reply, 'utf8'))
                    res += str(server_reply, 'utf8')
                    received_size += len(server_reply)
                else:
                    print("res:", res)
                    # print(str(server_reply.decode()))
                    print("------ reve doene -------")

    else:
        print("账户密码不对")

