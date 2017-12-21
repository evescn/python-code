#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 13:50
# @Author  : Evescn
# @Site    : 
# @File    : ftp_server.py
# @Software: PyCharm

import socket
import subprocess
import commons

if __name__ == '__main__':
    ip_port = ("127.0.0.1", 9999)

    sk = socket.socket()
    sk.bind(ip_port)
    sk.listen(5)

    while True:
        print("server is waiting...")
        conn, addr = sk.accept()
        while True:
            print("server is waiting...")
            client_data = conn.recv(1024)
            print("recv cmd:", str(client_data, 'utf8'))
            if not client_data:
                break
            print("recv cmd:", str(client_data, 'utf8'))
            # print(str(client_data, 'utf-8'))
            func_name = str(client_data, 'utf8')
            if func_name == 'login':    # 调用登录函数进行用户身份判断
                conn.send(client_data)
                username = conn.recv(1024)
                conn.send(username)
                username = str(username, 'utf8')

                passwd = conn.recv(1024)
                passwd = str(passwd, 'utf8')

                # print("username：", username)
                # print("passwd：", passwd)

                func = getattr(commons, func_name)  # commons.name 方法的内存地址
                result = func(username, passwd)
                # print("result：", result)
                result = str(result)
                # print(type(result))
                conn.send(bytes(result, 'utf8'))
                # print("OK")
            elif func_name == 'dir' or func_name == 'ls' or func_name == 'cd':  # 调用ls函数和cd函数
                func = getattr(commons, func_name)  # commons.name 方法的内存地址
                cmd_len, ack_msg, cmd_result = func()
                # return cmd_len, ack_msg, cmd_result
                print("cmd_result:", cmd_result)
                # print(type(cmd_result))
                conn.send(ack_msg)
                conn.recv(10)
                conn.send(cmd_result)
            else:   # 调用其他命令pwd之类的
                print("test is ok")
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
            # print("cmd is not fount")

