#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 21:57
# @Author  : Evescn
# @Site    : 
# @File    : shutil.py
# @Software: PyCharm

import shutil

# with open("test1.txt", 'rb') as f1:
#     with open("test2.txt", 'wb') as f2:
#         shutil.copyfileobj(f1, f2)
# shutil.copyfile("test1.txt", "test2.txt")

ret = shutil.make_archive("F:/GitHub/python-sp/day6/www", 'tar', root_dir='F:/GitHub/python-sp/day6/')

import zipfile
# z = zipfile.ZipFile('gm.zip', 'w')
# z.write('test1.txt')
# z.write('test2.txt')
# z.close()

# z = zipfile.ZipFile('gm.zip', 'r')
# z.extractall()
# z.close()