#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 22:48
# @Author  : Evescn
# @Site    : 
# @File    : re-lx.py
# @Software: PyCharm

import requests
import re

content = requests.get("https://book.douban.com").text
print(content)

pattern = re.compile(
    '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?"author">(.*?)</span>.*?"year">(.*?)</span>.*?</li>',
    re.S)

# results = re.findall('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?"author">(.*?)</span>.*?"year">(.*?)</span>.*?</li>', content, re.S)
results = re.findall(
    '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?/li>',
    content, re.S)
print(results)
