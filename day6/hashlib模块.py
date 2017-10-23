#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 15:26
# @Author  : Evescn
# @Site    : 
# @File    : hashlib模块.py
# @Software: PyCharm

import hashlib

hash = hashlib.md5()
hash.update("evescn".encode('utf-8'))
print(hash.hexdigest())

hash = hashlib.sha1()
hash.update("evescn".encode('utf-8'))
print(hash.hexdigest())

hash = hashlib.sha256()
hash.update("evescn".encode('utf-8'))
print(hash.hexdigest())

hash = hashlib.sha384()
hash.update("evescn".encode('utf-8'))
print(hash.hexdigest())

hash = hashlib.sha512()
hash.update("evescn".encode('utf-8'))
print(hash.hexdigest())

hash = hashlib.md5()
hash.update("evescn".encode('utf-8'))
print(hash.hexdigest())

hash = hashlib.md5()
hash.update(b"evescn")
print(hash.hexdigest())

hash = hashlib.md5("evescn".encode('utf-8'))
hash.update("evescn".encode('utf-8'))
print(hash.hexdigest())

import hmac

h = hmac.new(b"evescn")
h.update(b"evescn")
print(h.hexdigest())