#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 22:09
# @Author  : Shark
# @Site    : 
# @File    : 序列化-lx1.py
# @Software: PyCharm

import pickle

def login():
    print("This is test!")

f = open("user_acc.txt", "rb")
# data = pickle.loads(f.read())
data = pickle.load(f)
print(data)


print(type(data))
data['func']()

# import json
# f = open("user_acc.txt", "r")
# data = json.loads(f.read())