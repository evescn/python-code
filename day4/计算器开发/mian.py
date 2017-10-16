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
    print("ret=%d" %ret)
    return str(ret)


def chu():
    pass


def jiaorjian():
    pass


def jian():
    pass


def editstring():
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
    a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    a = a.replace(" ", "")
    # while True:
    b = re.findall('\([^\(\)]+\)', a)
    for i in range(len(b)):
        print(b[i])
        c = re.findall("[^\(\)]+", b[i])
        print(c)
        for i in range(len(c)):
            print(i)
            d = re.split("\-|\+", c[i])
            for i in d:
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
                        print("value=%s" % value)
                        a = a.replace(i, value)
                        print(a)

        print(a)
    b = re.findall('\([^\(\)]+\)', a)
    print(b)


if __name__ == '__main__':
    main()

