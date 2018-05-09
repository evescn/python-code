#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 14:42
# @Author  : Evescn
# @Site    : 
# @File    : SFTPClient.py
# @Software: PyCharm

import paramiko

transport = paramiko.Transport(('172.20.3.220', 22))
transport.connect(username='root', password='evescn')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('E:\GitHub\python-code\day9\private_key', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
# sftp.get('remove_path', 'local_path')

transport.close()