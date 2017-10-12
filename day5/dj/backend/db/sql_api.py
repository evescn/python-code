#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 12:25
# @Author  : evescn
# @Site    : 
# @File    : sql_api.py
# @Software: PyCharm

import sys
import os
base_dir = os.path.abspath(__file__)
for i in range(3):
    base_dir = os.path.dirname(base_dir)

sys.path.append(base_dir)

from config import settings


def db_auth(configs):
    if configs.DATABASE["user"] == "root" and configs.DATABASE["password"] == "123":
        print("db authentication succese!")
        return True
    else:
        print("db authentication error...")


def select(table, column):
    if db_auth(settings):
        if table == 'user':
            user_info = {
                "0":["root", 20],
                "1":["evescn", 22],
                "2":["gmkk", 22],
            }
            return user_info
    else:
        pass

