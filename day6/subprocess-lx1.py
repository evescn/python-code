#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 23:40
# @Author  : Evescn
# @Site    : 
# @File    : subprocess-lx1.py
# @Software: PyCharm

# import subprocess
#
# obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# obj.stdin.write('print("test")\n')
# obj.stdin.write('print("test2")\n')
# obj.stdin.write('print("test3")\n')
# obj.stdin.write('print("test4")\n')
# obj.stdin.close()
#
# cmd_out = obj.stdout.read()
# obj.stdout.close()
# cmd_error = obj.stderr.read()
# obj.stderr.close()
#
# print(cmd_out)
# print(cmd_error)

import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write("print('test')\n")
obj.stdin.write("print('test2')\n")
obj.stdin.write("print('test3')\n")
obj.stdin.write("print('test4')\n")
obj.stdin.write("print('test5')\n")

out_error_list = obj.communicate()
print(out_error_list)
# print("test")