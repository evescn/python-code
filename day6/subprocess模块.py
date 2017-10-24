#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 22:45
# @Author  : Evescn
# @Site    : 
# @File    : subprocess模块.py
# @Software: PyCharm

import subprocess

# subprocess.call("netstat")

# subprocess.call(["netstat", "-an"])
# subprocess.call("netstat -an", shell=True)

# subprocess.check_call("ls")

# subprocess.check_output(["echo", "Hello World!"])
# subprocess.check_output("df -h")

a = subprocess.Popen("netstat -an", shell=True, stdout=subprocess.PIPE)

print(a.stdout.read())