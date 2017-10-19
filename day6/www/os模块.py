#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 21:35
# @Author  : Evescn
# @Site    : 
# @File    : os.py
# @Software: PyCharm

import os
cwd = os.getcwd()
print(cwd)

# os.popen("dir")
# os.popen("dir").read()
# print(os.system("dir"))
# a = os.system("dir")
# print(a)
# a = os.popen("dir").read()   # 需要使用popen才能或者到执行命令的结果
# print(a)

ret = os.stat('os.py')
print(ret)

print(os.path.isfile('os.py'))
print(os.path.isdir('os.py'))
