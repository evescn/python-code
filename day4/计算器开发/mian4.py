#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 22:26
# @Author  : Shark
# @Site    : 
# @File    : mian4.py
# @Software: PyCharm

import re


def chengorchu(string):
    flag = True
    c = re.search(r'[^()]+', string)
    # print("c-c", c.group())
    ret1 = re.split("\*|\/", c.group())
    ret2 = re.findall("[\*\/]", c.group())
    # print("c-ret1:", ret1)
    # print("c-ret2:", ret2)
    if len(ret2) == 0:
        return ret1[0]
    for i in range(len(ret2)):
        if ret2[i] == '*':
            if flag:
                ret = float(ret1[0]) * float(ret1[1])
                flag = False
            else:
                ret *= float(ret1[i+1])
        else:
            if flag:
                ret = float(ret1[0]) / float(ret1[1])
                flag = False
            else:
                ret = ret / float(ret1[i+1])
    # print("test ret:", ret)
    return float(ret)


def jiaorjian(string):
    flag = True
    c = re.search(r'[^()]+', string)
    # print("j-c:", c.group())
    ret1 = re.split(r'\-|\+', c.group())
    ret2 = re.findall(r'\-|\+', c.group())
    # print("j-ret1:", ret1)
    # print("j-ret2:", ret2)
    if re.match(r'\-|\+', c.group()):
        if ret2[0] == "-":
            ret1[1] = -float(ret1[1])
        ret2 = ret2[1:]
        ret1 = ret1[1:]
        # print("j-ret1:", ret1)
        # print("j-ret2:", ret2)
        if len(ret2) == 0:
            return ret1[0]
    for i in range(len(ret2)):
        if ret2[i] == '+':
            if flag:
                ret = float(ret1[0]) + float(ret1[1])
                flag = False
            else:
                ret += float(ret1[i+1])
        else:
            if flag:
                ret = float(ret1[0]) - float(ret1[1])
                flag = False
            else:
                ret = ret - float(ret1[i+1])
    # print("ret=%d" %ret)
    return float(ret)


def deal_minus_issue(ret):
    # 处理减法字符串
    new_ret = []
    for index,item in enumerate(ret):
        if item.endswith("*") or item.endswith("/"):
            new_ret.append("%s-%s" %(ret[index], ret[index+1]))
        elif re.search("[*/]", ret[index]):
            new_ret.append(ret[index])
    # print("new_ret:", new_ret)
    return new_ret


def main():
    # 输入字符串
    a = '1 - 2 * ( (6-3 +(9-2*3/3 + 7/3*7/4*12 +10 * 5/5 )*(-5/5)) - (-4*3)/ (12-3*2) )'
    # a = '+(-40/5+3*(-12))'
    a = a.replace(" ", "")   #去空格
    flag = True
    count = 2
    while flag and count > 0:
        # 最内行括号
        ret = re.search(r'\([^()]+\)', a)
        # print("ret=", ret.group())
        if ret:
            # print("ret=", ret.group())
            ret_value = ret.group()
        else:
            count -= 1
            # print("count:", count)
            ret_value = a

        if "+" in ret_value or "-" in ret_value :
            if "*" in ret_value  or "/" in ret_value :
                c = re.findall(r'[^()]+', ret_value )
                # print(c)
                ret1 = re.split(r'[-+]', c[0])
                ret2 = re.findall(r'\-|\+', c[0])
                # print(ret1)
                # print(ret2)
                ret1 = deal_minus_issue(ret1)
                for i in ret1:
                    value = chengorchu(i)
                    # print("i:", i)
                    a = a.replace(i, str(value))
                    a = a.replace("+-", "-")
                    a = a.replace("--", "+")
                    # print("a:", a)
            else:
                value = jiaorjian(ret_value )
                a = a.replace(ret_value , str(value))
                a = a.replace("+-", "-")
                a = a.replace("--", "+")
                # print("a:", a)
        else:
            if "*" in ret_value  or "/" in ret_value :
                value = chengorchu(ret_value )
                a = a.replace(ret_value , str(value))
                a = a.replace("+-", "-")
                a = a.replace("--", "+")
                # print("a:", a)
            else:
                pass
        print("a:", a)

if __name__ == '__main__':
    main()