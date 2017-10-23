#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 17:23
# @Author  : Evescn
# @Site    : 
# @File    : time.py
# @Software: PyCharm
import time

# 返回处理器时间,3.3开始已废弃 , 改成了time.process_time()测量处理器运算时间,不包括sleep时间,不稳定,mac上测不出来
# print(time.clock())
# print(time.process_time())

# 返回与utc时间的时间差,以秒计算
# print(time.altzone)

# 返回时间格式"Thu Oct 19 17:26:06 2017"
# print(time.asctime())

# 返回本地时间 的struct time对象格式
# print(time.localtime())
# 返回时间格式"Fri Aug 19 11:14:16 2016"
# print(time.asctime(time.localtime()))
# 返回时间格式"Fri Aug 19 11:14:16 2016"
# print(time.ctime())

# 返回utc时间的struc时间对象格式
# print(time.gmtime(time.time()-800000))
# print(time.time())

# # 日期字符串 转成  时间戳
# # 将 日期字符串 转成 struct时间对象格式
# string_2_struct = time.strptime("2016/06/22", "%Y/%m/%d")
# string_2_struct = time.strptime("2016.06.22", "%Y.%m.%d")
# print(string_2_struct)
#
# # 将struct时间对象转成时间戳
# struct_2_stamp = time.mktime(string_2_struct)
# print(struct_2_stamp)
#
# # 返回时间格式"Fri Aug 19 11:14:16 2016"
# a = time.asctime(string_2_struct)
# print(a)

import datetime
# # 返回 2016-08-19 12:47:03.941925
# print(datetime.datetime.now())
# # 时间戳直接转成日期格式 2016-08-19
# print(datetime.date.fromtimestamp(time.time()))

# print(datetime.datetime.now())
# print(datetime.datetime.now()+datetime.timedelta(3))  # 当前时间+3天
# print(datetime.datetime.now()+datetime.timedelta(-3))  # 当前时间-3天
# print(datetime.datetime.now()+datetime.timedelta(hours=3))  # 当前时间+3小时
# print(datetime.datetime.now()+datetime.timedelta(minutes=30))  # 当前时间+30分

c_time = datetime.datetime.now()
print(c_time)
print(c_time.replace(minute=3, hour=2))

