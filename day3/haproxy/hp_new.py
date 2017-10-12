#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 16:26
# @Author  : evescn
# @Site    : edit haproxy.cfg file
# @File    : hp_new.py
# @Software: PyCharm

import json
import os
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


def fetch(backend):
    backend_title = 'backend %s' % backend
    record_list = []
    with open('ha') as obj:
        flag = False
        for line in obj:
            line = line.strip()
            if line == backend_title:
                flag = True
                continue
            if flag and line.startswith('backend'):
                flag = False
                break

            if flag and line:
                record_list.append(line)

    return record_list


def add(dict_info):
    backend = dict_info.get('backend')
    record_list = fetch(backend)
    # print(record_list)
    sign = 1
    backend_title = "backend %s" % backend
    current_record = "server %s %s weight %d maxconn %d" % (dict_info['record']['server'], dict_info['record']['server'], dict_info['record']['weight'], dict_info['record']['maxconn'])
    if not record_list:
        record_list.append(backend_title)
        record_list.append(current_record)
        with open('ha') as read_file, open('ha.new', 'w') as write_file:
            flag = False
            for line in read_file:
                write_file.write(line)
            for i in record_list:
                if i.startswith('backend'):
                    write_file.write(i + '\n')
                else:
                    write_file.write("%s%s\n" % (8 * " ", i))
    else:
        record_list.insert(0, backend_title)
        # print(record_list)
        if current_record not in record_list:
            record_list.append(current_record)
            with open('ha') as read_file, open('ha.new', 'w') as write_file:
                flag = False
                has_write = False
                for line in read_file:
                    line_strip = line.strip()
                    if line_strip == backend_title:
                        flag = True
                        continue
                    if flag and line_strip.startswith('backend'):
                        flag = False
                    if not flag:
                        write_file.write(line)
                    else:
                        if not has_write:
                            for i in record_list:
                                if i.startswith('backend'):
                                    write_file.write(i + '\n')
                                else:
                                    write_file.write("%s%s\n" % (8 * " ", i))
                        has_write = True
        else:
            sign = 0
            print("该IP记录已存在，请重新确认信息")
    if sign == 1:
        move_filename()


def remove(dict_info):
    backend = dict_info.get('backend')
    record_list = fetch(backend)
    backend_title = "backend %s" % backend
    current_record = "server %s %s weight %d maxconn %d" % (dict_info['record']['server'], dict_info['record']['server'], dict_info['record']['weight'], dict_info['record']['maxconn'])
    if not record_list:
        print("该backend记录不在配置文件中，请检测后重新输入！")
        return
    else:
        if current_record not in record_list:
            print("该主机配置记录不正确，请检测后重新输入！")
            return
        else:
            del record_list[record_list.index(current_record)]
            if len(record_list) > 0:
                record_list.insert(0, backend_title)
        with open('ha') as read_file, open('ha.new', 'w') as write_file:
            flag = False
            has_write = False
            for line in read_file:
                line_strip = line.strip()
                if line_strip == backend_title:
                    flag = True
                    continue
                if flag and line_strip.startswith('backend'):
                    flag = False
                if not flag:
                    write_file.write(line)
                else:
                    if not has_write:
                        for i in record_list:
                            if i.startswith('backend'):
                                write_file.write(i + '\n')
                            else:
                                write_file.write("%s%s\n" % (8 * " ", i))
                    has_write = True
    move_filename()


def move_filename():
    for file in os.listdir('.'):
        if file == "ha.bak":
            os.remove(file)
    os.rename('ha', 'ha.bak')
    os.rename('ha.new', 'ha')
    print("操作成功")


def show():
    # 显示信息函数
    print("*****************************")
    print("1、获取ha记录")
    print("2、增加ha记录")
    print("3、删除ha记录")
    print("4、退出系统")
    print("*****************************")
    return

@login
def main():
    while True:
        # 输出显示信息
        show()

        num = input('请输入序号：')

        if num == '1':
            data = input('请输入内容：')
            ret = fetch(data)
            for i in ret:
                print(i)
        elif num == '4':
            sys.exit("欢迎再次使用haproxy修改系统")
        else:
            data = input('请输入内容：')
            dict_data = json.loads(data)
            if num == '2':
                add(dict_data)
            elif num == '3':
                remove(dict_data)
            else:
                print("你输入的操作系列号有误！请重新输入。")


if __name__ == '__main__':
    main()
