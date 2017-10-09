#!/usr/bin/env python
# -*- conding:utf-8 -*-
# edit haproxy file  Additions Deletions Modification Inquire

# 20171009
# evescn


import json
import os
import yaml
import sys


def login(func):
    def loginning(*args,**kwargs):
        # 验证用户帐号和密码函数
        # global name
        lock = "lock.txt"
        loginfile = "password.txt"
        login_info = 0
        i = 0

        while i < 3 and login_info == 0:
            name = input("Please input your name: ")
            with open(lock, "r") as f:
                for line in f:
                    # if name in line:
                    if name == line.strip():
                        sys.exit('\033[32:1m用户 %s 已经被锁定\033[0m' % name)
            password = input("Please input password: ")
            with open(loginfile, "r") as f:
                for line in f:
                    user_file, pass_file = line.split()
                    if user_file == name and pass_file == password:
                        # print("Bingo!")
                        login_info = 1
                        continue
                else:
                    if login_info != 1:
                        print("You name or password is error!")
                        i += 1
        else:
            if i == 3 and login_info == 0:
                f = open(lock, "a")
                f.write(name + "\n")
                f.close()
                print('\033[32:1m用户 %s 已经被锁定\033[0m' % name)
        return func(*args, **kwargs)
    return loginning


def show():
    # 显示信息函数
    print("*****************************")
    print("1、获取ha记录")
    print("2、增加ha记录")
    print("3、删除ha记录")
    print("4、退出系统")
    print("*****************************")
    return


def inquire():
    read = input('请输入backend：')
    sign = 0

    with open("haproxy.cfg", "r") as f1:
        for line in f1:
            text = line.split()
            if sign == 1:
                if not text:
                    sign = 0
                elif "backend" in text:
                    sign = 0
                else:
                    print(str(text))
            if "backend" in text:
                if text[1] == read:
                    sign = 1


def additions():
    read = input('请输入要新加的记录：')
    read_dict = json.loads(read)
    sign = 0

    backend_title = read_dict['backend']
    backend_record = read_dict['record']
    with open("haproxy.cfg", "r") as f1:
        with open("tmp.txt", "w") as f2:
            for line in f1:
                text = line.split()
                if sign == 1:
                    # 判断该记录是否已存在
                    if not text:
                        sign = 2
                        continue
                    elif "backend" in text:
                        sign = 2
                    elif str(backend_record['server']) == str(text[1]):
                        print("该IP记录已存在，请重新确认信息")
                        return
                elif sign == 2:
                    # 若该记录不存在则添加该记录
                    text = '        server %s %s weight %s maxconn %s' % (backend_record['server'], backend_record['server'], backend_record['weight'], backend_record['maxconn'])
                    dat_out = "".join(text)
                    f2.write(dat_out + "\n")
                    f2.write("\n")
                    print("新增记录成功")
                    sign = 3

                if "backend" in text:
                    # 找到修改配置的位置
                    if text[1] == str(backend_title):
                        sign = 1
                        dat_out = "".join(line)
                        f2.write(dat_out)
                    else:
                        dat_out = "".join(line)
                        f2.write(dat_out)
                else:
                    dat_out = "".join(line)
                    f2.write(dat_out)

            if sign == 0:
                title = "%s %s" % ("backend", backend_title)
                dat_out = "".join(title)
                f2.write(dat_out + "\n")

                text = '        server %s %s weight %s maxconn %s' % (backend_record['server'], backend_record['server'], backend_record['weight'], backend_record['maxconn'])
                dat_out = "".join(text)
                f2.write(dat_out + "\n")
                print("新增记录成功")

    move_filename("haproxy.cfg")


def deletions():
    read = input('请输入要删除的记录：')
    read_dict = json.loads(read)
    sign = 0

    backend_title = read_dict['backend']
    backend_record = read_dict['record']
    with open("haproxy.cfg", "r") as f1:
        with open("tmp.txt", "w") as f2:
            for line in f1:
                text = line.split()
                if sign == 1:
                    if not text:
                        sign = 0
                    elif "backend" in text:
                        sign = 0
                    elif str(backend_record['server']) == str(text[1]) and str(backend_record['weight']) == str(text[4]) and str(backend_record['maxconn']) == str(text[6]):
                        print("删除成功")
                        continue
                if "backend" in text:
                    if text[1] == str(backend_title):
                        sign = 1
                    else:
                        dat_out = "".join(line)
                        f2.write(dat_out)
                else:
                    dat_out = "".join(line)
                    f2.write(dat_out)
    move_filename("haproxy.cfg")

    with open("haproxy.cfg", "r") as f1:
        with open("tmp.txt", "w") as f2:
            for line in f1:
                text = line.split()
                if sign == 1:
                    if not text:
                        sign = 0
                    elif "backend" in text:
                        sign = 0
                if "backend" in text:
                    if text[1] == str(backend_title):
                        if not text:
                            continue
                        sign = 1
                    else:
                        dat_out = "".join(line)
                        f2.write(dat_out)
                else:
                    dat_out = "".join(line)
                    f2.write(dat_out)
    move_filename("haproxy.cfg")


def move_filename(filename):
    # 重命名文件名函数
    for file in os.listdir('.'):  # os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
        if file == filename:
            os.remove(file)
    for file in os.listdir('.'):
        if file == "tmp.txt":
            new_name = filename
            os.rename(file, new_name)
            return


@login
def main():
    while True:
        # 输出显示信息
        show()

        key =  input("请输入操作序号：")
        if key == '1':
            inquire()
        elif key == '2':
            additions()
        elif key == '3':
            deletions()
        elif key == '4':
            sys.exit("欢迎再次使用haproxy修改系统")
        else:
            print("你输入的操作系列号有误！请重新输入。")


if __name__ == "__main__":
    main()
