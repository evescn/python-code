#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: ??
@author: evescn
@license: Apache Licence
@file: handle.py
@time: 2017/10/11 22:45
"""

from backend.db.sql_api import select


def home():
    print("welcome to home page")
    user_data = select("user", "12")
    print(user_data)


def movie():
    print("welcome to movie page")


def tv():
    print("welcome to tv page")


