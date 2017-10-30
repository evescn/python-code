#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 21:21
# @Author  : Evescn
# @Site    : 
# @File    : log-lx1.py
# @Software: PyCharm

import logging

# logging.basicConfig(filename="log.txt", level=logging.INFO)
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.basicConfig(filename="log.txt", level=logging.INFO, format='%(asctime)s: %(message)s', datefmt='%Y-%d-%m  %I:%M:%S %p')
# logging.debug("This message shoudl go to the log file")
# logging.info("So should this")
# logging.warning("And this, too")

logging.basicConfig(filename="log.txt", format='%(asctime)s : %(message)s', datefmt='%Y-%d-%m %I:%M:%S', level=logging.INFO)
logging.debug("1")
logging.info("2")
logging.warning("3")