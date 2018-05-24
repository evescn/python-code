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

# pattern = re.compile(
#     '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?"author">(.*?)</span>.*?"year">(.*?)</span>.*?</li>',
#     re.S)

# pattern = re.compile('<li.*?cover.*?href="(.*?)"\stitle="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?/li>',re.S)
#
# # results = re.findall('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?"author">(.*?)</span>.*?"year">(.*?)</span>.*?</li>', content, re.S)
# results = re.findall(pattern, content)
# print(results)

# for result in results:
#     url, name, author, data = result
#     author=re.sub('\s', '', author)
#     data=re.sub('\s', '', data)
#     print(url, name, author, data)


content = requests.get('https://book.douban.com/').text
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)

print(results)