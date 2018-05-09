#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 14:36
# @Author  : Evescn
# @Site    : 
# @File    : paramiko_key.py
# @Software: PyCharm

import paramiko

ckey = 'E:\GitHub\python-code\day9\private_key'
private_key = paramiko.RSAKey.from_private_key_file('/home/evescn/.ssh/id_rsa')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='172.20.3.220', port=22, username='evescn', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
result = stdout.read()

# 关闭连接
ssh.close()