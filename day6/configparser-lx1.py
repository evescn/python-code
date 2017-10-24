#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 16:35
# @Author  : Evescn
# @Site    : 
# @File    : configparser-lx1.py
# @Software: PyCharm

import configparser

config = configparser.ConfigParser()
print(config.sections())

config.read("example.ini")

print(config.sections())
print(config.defaults())
print(config.default_section)

ret = 'bitbucket.org' in config
print(ret)

ret = 'bytebong.com' in config
print(ret)

print(config['bitbucket.org']['User'])

print(config['DEFAULT']['Compression'])

topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])
print(topsecret['host port'])

for key in config['bitbucket.org']:
    print(key)
