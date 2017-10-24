#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 12:25
# @Author  : Evescn
# @Site    : 
# @File    : configparser-lx2.py
# @Software: PyCharm

# [section1]
# k1 = v1
# k2: v2
#
# [section2]
# k1 = v1

import configparser

config = configparser.ConfigParser()
config.read('example.ini')

# ########## 读 ##########
# secs = config.sections()
# print secs
# options = config.options('group2')
# print options

# item_list = config.items('group2')
# print item_list

# val = config.get('group1','key')
# val = config.getint('group1','key')

# ########## 改写 ##########
# sec = config.remove_section('bitbucket.org')
# config.write(open('example2.cfg', "w"))

# sec = config.has_section('evescn')
# sec = config.add_section('evescn')
# config.add_section('evescn')
# config['evescn']['age'] = '22'
# config.write(open('example3.cfg', "w"))


# config.set('bitbucket.org', 'User', "evescn")
# config.write(open('example4.cfg', "w"))

# config.remove_option('bitbucket.org', 'User')
# config.write(open('example5.cfg', "w"))