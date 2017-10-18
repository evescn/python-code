#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 16:27
# @Author  : evescn
# @Site    : 
# @File    : mian2.py
# @Software: PyCharm


import re


def chengorchu(ret1, ret2):
    flag = True
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
    return float(ret)


def jiaorjian(ret1, ret2):
    flag = True
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
    print("ret=%d" %ret)
    return float(ret)


def delstring():
    pass


def stringex(string, a):
    print(string)
    ret = re.split("\-|\+", string)
    print(ret)
    for i in ret:
        print(i)
        if i == "":
            # print("Null")
            continue
        else:
            ret1 = re.split("\*|\/", i)
            ret2 = re.findall("[\*\/]", i)
            print(ret1)
            print(ret2)
            if ret2:
                value = chengorchu(ret1, ret2)
                print("value=%s" %value)

                a = a.replace(i, value)
                print(a)


def main():
    # 输入字符串
    a = '1 - 2 * ( (6-3 +(5/5) * (9-2*3/3 + 7/3*7/4*12 +10 * 5/5 )) - (-4*3)/ (12-3*2) )'
    # a = '+(-40/5+3*12)'
    a = a.replace(" ", "")   #去空格
    flag = True
    while flag:
        # 最内行括号
        ret = re.search(r'\([^()]+\)', a)
        if not ret:
            flag = False
            continue
        print("ret=", ret.group())
        # b = ret.group()
        # print(b)
        # print(type(b))
        if "+" in ret.group() or "-" in ret.group():
            if "*" in ret.group() or "/" in ret.group():
                sz = []
                c = re.findall(r'[^()]+', ret.group())
                # print(c)
                ret1 = re.split(r'\-|\+', c[0])
                ret2 = re.findall(r'\-|\+', c[0])
                print(ret1)
                print(ret2)
                for j in ret1:
                    if j == "":
                        continue
                    else:
                        ret3 = re.split("\*|\/", j)
                        ret4 = re.findall("[\*\/]", j)
                        if ret4:
                            value = chengorchu(ret3, ret4)
                            print("value=%s" % value)
                            sz.append(value)
                            print("3", sz)
                        else:
                            print()
                            sz.append(float(j))

                if len(sz) > len(ret2):
                    print("sz>2")
                    value = jiaorjian(sz, ret2)
                    a = a.replace(ret.group(), str(value))
                    print("4", a)
                else:
                    if len(ret2) > 1:
                        ret5 = ret2[1:]
                        print(ret5)
                        value = jiaorjian(sz, ret5)
                    if ret2[0] == "-":
                        sz[0] = -sz[0]
                        if len(ret2) > 1:
                            ret5 = ret2[1:]
                            value = jiaorjian(sz, ret5)
                            print(value)
                        else:
                            value = sz[0]
                    a = a.replace(ret.group(), str(value))
                    print(a)
                    a = a.replace("+-", "-")
                    a = a.replace("--", "+")
                    print("4gm", a)
            else:
                sz = []
                c = re.findall(r'[^()]+', ret.group())
                # print(c)
                ret1 = re.split(r'\-|\+', c[0])
                ret2 = re.findall(r'\-|\+', c[0])
                if len(ret1) > len(ret2):
                    # print("sz>2")
                    value = jiaorjian(sz, ret2)
                    a = a.replace(ret.group(), str(value))
                    # print("4", a)
                else:
                    if len(ret2) > 1:
                        ret5 = ret2[1:]
                        print(ret5)
                        value = jiaorjian(sz, ret5)
                    if ret2[0] == "-":
                        sz[0] = -sz[0]
                        if len(ret2) > 1:
                            ret5 = ret2[1:]
                            value = jiaorjian(sz, ret5)
                            print(value)
                        else:
                            value = sz[0]
                    a = a.replace(ret.group(), str(value))
                    print(a)
                    a = a.replace("+-", "-")
                    a = a.replace("--", "+")
        else:
            if "*" in ret.group() or "/" in ret.group():
                sz = []
                c = re.findall(r'[^()]+', ret.group())
                print("2b", c)
                ret3 = re.split("\*|\/", c[0])
                ret4 = re.findall("[\*\/]", c[0])
                print("2ret3", ret3)
                print("2ret4", ret4)
                if ret4:
                    value = chengorchu(ret3, ret4)
                    print("value=%s" % value)
                    sz.append(value)
                    print("3", sz)
                # else:
                #     print()
                #         sz.append(float(j))

                a = a.replace(ret.group(), str(value))
                print("4b", a)
            else:
                if len(ret2) > 1:
                    ret5 = ret2[1:]
                    print(ret5)
                    value = jiaorjian(sz, ret5)
                if ret2[0] == "-":
                    sz[0] = -sz[0]
                    if len(ret2) > 1:
                        ret5 = ret2[1:]
                        value = jiaorjian(sz, ret5)
                        print(value)
                    else:
                        value = sz[0]
                a = a.replace(ret.group(), str(value))
                print(a)
                a = a.replace("+-", "-")
                a = a.replace("--", "+")
                print("4gm", a)



if __name__ == '__main__':
    main()