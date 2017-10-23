#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 21:22
# @Author  : Evescn
# @Site    : 
# @File    : re模块.py
# @Software: PyCharm

import re

# obj = re.match('\d+', '957evescn')
# if obj:
#     print(obj.group())


# import re
#
# obj = re.search('\d+', 'gmkk957evescn')
# if obj:
#     print(obj.group())

# a = "123abc456"
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group())
#
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0))
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1))
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2))
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(3))
#
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).groups())


import re

# obj = re.findall('\D+', 'evescn666gmkk')
# print(obj)

# content = "123abc456"
# new_content = re.sub('\d+', 'sb', content)
# # new_content = re.sub('\d+', 'sb', content, 1)
# print(new_content)

import re

content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
new_content = re.split('\*', content)
# new_content = re.split('\*', content, 1)
print(new_content)

content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
# new_content = re.split('[\+\-\*\/]+', content)
new_content = re.split('[\+\-\*\/]+', content, 1)
print(new_content)

inpp = '1-2*((60-30 +(-40-5)*(9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))'
inpp = re.sub('\s*', '', inpp)
print(inpp)
new_content = re.split('\(([\+\-\*\/]?\d+[\+\-\*\/]?\d+){1}\)', inpp, 1)
print(new_content)