#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 21:32
# @Author  : Evescn
# @Site    : 
# @File    : random.py
# @Software: PyCharm

import random

print(random.random())
ret = random.randint(1, 100)
print(ret)
print(type(ret))

ret = random.randrange(1, 100)
print(ret)
print(type(ret))

checkcode = ''
for i in range(6):
    current = random.randrange(0, 6)
    if current != i:
        temp = chr(random.randint(65, 90))
    else:
        temp = random.randint(0, 9)

    checkcode += str(temp)
print(checkcode)