#!/usr/bin/env pyton
# -*- coding:utf-8 -*-
import re

# re.match(pattern, data_source)
m = re.match("abc", "abcdfe")   # 从开头开始匹配
print(m.group())

m = re.match("[0-9]*", "12abc123")
if m:
    print(m.group())
m = re.match("[0-9]{0,1}", "12abc123")
if m:
    print(m.group())

m = re.findall("[0-9]{1,10}", "123abc123")    # 所有符合添加均匹配
m = re.findall("[a-zA-Z]{1,10}", "123sdf452saf")
m = re.findall(".+", "123sdf452saf")
if m:
    print(m)

m = re.search("\d+", "75_46.5 4a~bc6@def")   #查找到第一次符合条件的结果
m = re.search("\d+", "abc75_46.5 4a~bc6@def")
if m:
    print(m.group())

m = re.sub("\d+", "|", "abc75_46.5 4a~bc6@def")
m = re.sub("\d+", "|", "abc75_46.5 4a~bc6@def", count=2)
if m:
    print(m)


