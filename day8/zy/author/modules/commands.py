#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 11:01
# @Author  : Evescn
# @Site    : 
# @File    : commands.py
# @Software: PyCharm

"""
__author: wangsong
命令处理模块，对用户输入的命令进行分析、处理、并返回结果
"""

import sys
import os
import paramiko
from multiprocessing import Pool
from modules.myexception import MyException
from modules.common import write_log
from dbhelper import dbapi
from modules.users import Users
from conf import settings

__command__ = ["show", "cmd", "sftp", "help"]

def exec_cmd(userobj, input_command):
    """

    :param userobj:
    :param input_command:
    :return:
    """
    try:
        # 获取第一个命令指令
        command_list  = input_command.split()
        command = command_list[0]
        if command not in __command__:
            raise MyException("103")
        else:
            # 调用对应的命令
            func = getattr(sys.modules[__name__], command)
            func(userobj, command_list)

    except MyException as e:
        write_log(e, "warning")
        print(e)
    except Exception as e:
        write_log(e, "error")

def show(userobj, input_command_list):
    """
    执行show命令，查看当前用户管理的所有服务器信息,可用命令：
        show hosts -a : 查看所有服务器IP、主机名、所属组
        show hosts -g gid: 查看组id（gid) 对应的所有主机信息
        show groups: 查看当前用户管理的所有组
    如果show跟其它参数 不认识
    :param userobj:  用户对象
    :param input_command_list: 用户输入的命令,split后的列表
    :return: 返回结果信息
    """
    try:
        show_args = ["hosts", "groups"]

        if len(input_command_list) < 2:
            raise MyException("106")
        else:
            input_args = input_command_list[1]

            if input_args == "hosts":
                # 如果有-a
                if input_command_list.count("-a") > 0:
                    if len(input_command_list) > 3:
                        raise MyException("103")
                    else:
                        # 显示所以主机信息
                        user_gid_list = userobj.groups.aplit(".")

                # 没有 -a，有 -g 吗
                elif input_command_list.count("-g") > 0:
                    user_gid_list = input_command_list[input_command_list.index("-g") + 1].split(",")
                else:
                    raise MyException("103")

                for gid in user_gid_list:
                    # 根据用户的组ID，获取对应的host信息字典
                    hosts_info = dbapi.load_host_by_gid(gid)
                    for host in hosts_info:
                        print("\033[1;30m \nIP: {0}  主机名: {1}  所属组ID: {2} \033[0m;".format(host["ip"],
                                                                                           host["hostname"],
                                                                                           gid))

            elif input_args == "groups":
                # 打印所有组信息
                user_gid = userobj.groups
                groups_dict = dbapi.load_group_info()
                # 从所有组信息中删除不在用户gid中的元素，剩下打印
                _total_gid_list = list(groups_dict.keys())
                for gid in _total_gid_list:
                    if gid not in user_gid.split(","):
                        del groups_dict[gid]

                #显示用户组信息
                for k, v in groups_dict.items():
                    print("\033[1;30m GID: {0}, GNAME: {1}\033[0m;\n".format(k, v))

            else:
                raise  MyException("106")

    except MyException as e:
        write_log(e, "error")
        print(e)
    except Exception as e:
        write_log(e, "error")

@Users.auth_ip
def cmd(userobj, input_command_list):
    """
    在管理的服务器上执行cmd命令，命令支持:
    cmd -h 192.168.1.100,192.168.1.200 -c "df -hl"
    cmd -g G01 -c "df -hl"
    :param userobj:
    :param input_command_list:
    :return:
    """
    # 命令

    command_str = ""
    try:
        # 有命令吗?有的话-c后面的元素在" "之间的都是命令
        if input_command_list.count("-c") > 0:
            start_index = input_command_list.index("-c") + 1
            end_index = len(input_command_list)
            for cmd_str in input_command_list[start_index:end_index]:
                command_str += " {0}".format(cmd_str)
                if cmd_str.endseith('"'):
                    break
            # 去前后的双引号
            command_str = command_str.replace('"', '')
        else:
            raise MyException("106")