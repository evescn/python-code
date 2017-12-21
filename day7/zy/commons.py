#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 14:04
# @Author  : Evescn
# @Site    : 
# @File    : commons.py
# @Software: PyCharm

import subprocess
from prettytable import PrettyTable


def login(username, passwd):
    print("这个是登录函数")
    with open("password.txt", 'r') as f:
        for line in f:
            user_file, pass_file, homedir, disksize = line.split()
            print("homedir:%s" % homedir)
            if user_file == username and pass_file == passwd:
                print("Bingo!")
                login_info = 1
                return 0
        else:
            print("You name or password is error!")
            return 1
    a = subprocess.Popen("cd homedir && pwd", shell=True, stdout=subprocess.PIPE)
    print(a.stdout.read())


def showinfo(key):
    if key == 'login':
        print("请输入用户：")
        username = input(">：")
        print("请输入密码：")
        password = input(">：")
        return username, password
    elif key == 'show':
        x = PrettyTable(["命令", "结果"])
        x.align["命令"] = "l"  # 以name字段左对齐
        x.align["结果"] = "l"  # 以name字段右对齐
        x.padding_width = 1  # 填充宽度
        with open("cmd.txt", "r", encoding='utf-8') as f:
            for line in f:
                cmd, info = line.split()
                x.add_row([cmd, info])
            print(x)
        cmd = input("请输入命令:>")
        return cmd


def ls():
    print("这个是ls函数")
    cmd_len, ack_msg, cmd_result = commond('ls')
    return cmd_len, ack_msg, cmd_result


def dir():
    print("这个是wdir函数")
    cmd_len, ack_msg, cmd_result = commond('dir')
    return cmd_len, ack_msg, cmd_result


def cd():
    print("这个是cd函数")
    cmd_len, ack_msg, cmd_result = commond('cd')
    return cmd_len, ack_msg, cmd_result


def commond(cmd):
    cmd_call = subprocess.Popen(cmd, cwd="/home/evescn", shell=True, stdout=subprocess.PIPE)
    cmd_result = cmd_call.stdout.read()
    if len(cmd_result) == 0:
        cmd_result = b'commond is not found'
    cmd_len = len(cmd_result)
    ack_msg = bytes("CMD_RESULT_SIZE|%s" % len(cmd_result), 'utf8')
    return cmd_len, ack_msg, cmd_result


def get():
    print("这个是get函数")


def put():
    print("这个是put函数")
