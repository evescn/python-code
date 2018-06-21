#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-6-20 下午4:24
# @Author  : Evescn
# @Site    : 
# @File    : jsonload.py
# @Software: PyCharm Community Edition
import json

with open('need.json', 'r') as f:
    temp = f.read()
    # print(temp)
    # temp = temp.decode("gbk").encode("utf-8")
    dic = json.loads(temp)

    print(dic)
    # print(dic['ffffd7c225494ceba36bcf31fb31de8e'])

    dic = { 'a': [1, 2], 'b': [3, 4]}

    print(dic['a'][0])
    print(dic['a'][1])