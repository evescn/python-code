#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 9:43
# @Author  : Evescn
# @Site    : 
# @File    : settings.py
# @Software: PyCharm

"""
__author: super
blog: http://blog.csdn.net/songfreeman
系统配置文件
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))

# 数据库文件
DB_FILE_PATH = os.path.join(BASE_DIR, "dbstore")
DB_USERS = os.path.join(DB_FILE_PATH, "user.xml")
DB_GROUPS = os.path.join(DB_FILE_PATH, "groups.xml")
DB_HOSTS = os.path.join(DB_FILE_PATH, "hosts.xml")

# 日志记录文件
SYSLOG_FILE = os.path.join(BASE_DIR, "logs/syslog.log")
OPLOG_FILE = os.path.join(BASE_DIR, "logs/oplog.log")

# 日志输出级别 info, debug, error, warning
LOG_LEVEL = "info"

# 是否打印到屏幕
LOG_PRING = False

# 私钥存放目录
RSAKEY = os.path.join(BASE_DIR, "sshkey")
