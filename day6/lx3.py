#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 22:37
# @Author  : Evescn
# @Site    : 
# @File    : lx3.py
# @Software: PyCharm

import logging
logger = logging.getLogger("Eevescn-Test")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)


fh = logging.FileHandler("access1.log")
fh.setLevel(logging.INFO)

formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter2 = logging.Formatter('%(asctime)s - GMKK - %(levelname)s - %(message)s')

ch.setFormatter(formatter1)
fh.setFormatter(formatter2)

logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
