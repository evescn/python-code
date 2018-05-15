#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: ??
@author: evescn
@license: Apache Licence
@file: handle.py
@time: 2017/10/11 22:45
"""
#
# import sys
# import os
# base_dir = os.path.abspath(__file__)
# for i in range(2):
#     base_dir = os.path.dirname(base_dir)
#
# sys.path.append(base_dir)
# print(base_dir)

# from db.sql_api import select
from backend.db import sql_api as sq
# from db import sql_api as sq


def home():
    print("welcome to home page")
    user_data = sq.select("user", "12")
    print(user_data)


def movie():
    print("welcome to movie page")


def tv():
    print("welcome to tv page")


home()