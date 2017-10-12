#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 22:01
# @Author  : Shark
# @Site    : 
# @File    : 序列化.py
# @Software: PyCharm

import pickle

def login():
    print("This is login!")

f = open("user_acc.txt", "wb")


info = {
    "evescn":"1",
    "gmkk":"2",
    "func":login
}

# print(pickle.dumps(info))
# f.write(pickle.dumps(info))
pickle.dump(info,f)
f.close()

# import json
# f = open("user_acc.txt", "w")
# f.write(json.dumps(info))
# f.close()