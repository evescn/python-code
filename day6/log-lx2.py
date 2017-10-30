#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 22:12
# @Author  : Evescn
# @Site    : 
# @File    : log-lx2.py
# @Software: PyCharm

import logging

# create logger
logger = logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)   # 全局定义，全局优先级最高，并且设置下面所有句柄的最高可捕捉的日志级别

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create file handler and set level to warning
fh = logging.FileHandler("access.log")
fh.setLevel(logging.WARNING)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')