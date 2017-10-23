#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 21:35
# @Author  : Evescn
# @Site    : 
# @File    : os.py
# @Software: PyCharm

import os
# cwd = os.getcwd()
# print(cwd)

# os.makedirs("evescn/evescn")
# os.removedirs("evescn/evescn")

# os.mkdir("evescn")
# os.rmdir("evescn")

# ret = os.listdir()
# print(ret)

# os.remove("www.tar")

# os.rename("test2.txt", "test3.txt")
# os.rename("test3.txt", "test2.txt")

# print(os.sep)
# ret = os.linesep
# print(list(ret))
# print(os.pathsep)
# print(os.name)

# os.popen("dir")
# os.popen("dir").read()
# print(os.system("dir"))
# a = os.system("dir")
# print(a)
# a = os.popen("dir").read()   # 需要使用popen才能或者到执行命令的结果
# print(a)

# ret = os.stat('os模块.py')
# print(ret)

# print(os.path.isfile('os.py'))
# print(os.path.isdir('os.py'))

# print(os.environ)
# print(os.path.abspath("./"))

# path, file = os.path.split(os.path.abspath(os.getcwd()))
# print(path)
# print(file)

print(os.path.dirname(os.getcwd()))
print(os.path.basename(os.getcwd()))

print(os._exists("E:\GitHub"))

# print(os.)