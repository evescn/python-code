#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 11:23
# @Author  : evescn
# @Site    : 
# @File    : mian.py
# @Software: PyCharm

import re


def chengorchu(ret1, ret2):
    flag = True
    for i in range(len(ret2)):
        if ret2[i] == '*':
            if flag:
                ret = int(ret1[0]) * int(ret1[1])
                flag = False
            else:
                    # ret = int(ret) * int(ret1[i])
                ret *= int(ret1[i+1])
        else:
            if flag:
                ret = int(ret1[0]) / int(ret1[1])
                flag = False
            else:
                # ret = int(ret) * int(ret1[i])
                # print(ret)
                ret = ret / int(ret1[i+1])
    # print("ret=%d" %ret)
    return str(ret)


def jiaorjian(ret1, ret2):
    flag = True
    for i in range(len(ret2)):
        if ret2[i] == '+':
            if flag:
                ret = int(ret1[0]) + int(ret1[1])
                flag = False
            else:
                ret += int(ret1[i+1])
        else:
            if flag:
                ret = int(ret1[0]) - int(ret1[1])
                flag = False
            else:
                ret = ret - int(ret1[i+1])
    # print("ret=%d" %ret)
    return str(ret)


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
    a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    a = a.replace(" ", "")   #去空格
    # while True:

    # 最内行括号
    b = re.findall('\([^\(\)]+\)', a)
    for i in range(len(b)):
        print("1 ", b[i])
        if "+" in b[i] or "-" in b[i]:
            # print("AOK")
            if "*" in b[i] or "/" in b[i]:
                sz = []
                c = re.findall("[^\(\)]+", b[i])
                print("2 %s" %c)
                for i in range(len(c)):
                    ret1 = re.split("\-|\+", c[i])
                    ret2 = re.findall("\-|\+", c[i])
                    # print("ret %s" %ret)
                    print(ret1)
                    print(ret2)
                    for i in ret1:
                        print(i)
                        if i == "":
                            continue
                        # elif i != :
                        #     sz.append(i)
                        else:
                            ret3 = re.split("\*|\/", i)
                            ret4 = re.findall("[\*\/]", i)
                            if ret4:
                                value = chengorchu(ret3, ret4)
                                print("value=%s" % value)
                                sz.append(value)
                                print("3", sz)
                                # a = a.replace(i, value)
                                # print(a)
                else:
                    if len(sz)  > len(ret2):
                        value = jiaorjian(sz, ret2)
                        a = a.replace(c[i], value)
                    else:
                        # a = a.replace(c[i], int(sz[0]))
                        print("4 ", a)
            else:
                c = re.findall("[^\(\)]+", b[i])
                for i in range(len(c)):
                    ret1 = re.split("\-|\+", b[i])
                # print("ret1", ret1)
        else:
            pass


if __name__ == '__main__':
    main()

