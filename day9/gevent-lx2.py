#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 11:49
# @Author  : Evescn
# @Site    : 
# @File    : gevent-lx2.py
# @Software: PyCharm

from gevent import monkey;

monkey.patch_all()
import gevent
from urllib.request import urlopen


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])