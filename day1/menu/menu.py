#!/usr/bin/env python
# -*- conding:utf-8 -*-
# create a menu system

# 20170911
# evescn

import sys
import yaml


def myinput():
    # 输出提示信息的函数
    print("输入q退出系统")
    print("输入b返回上一级菜单")
    key = input("请输入对应的名称进入下级菜单：")
    return key


def mycity(key):
    # 输出市级别信息的函数
    print("-------------------------------------------------")
    for i, m in enumerate(menu[str(key)], 1):
        for item in m.keys():
            print("    ", i, item)
    key = myinput()
    return key


def mycounty(key1, key2):
    # 输出县基本信息的函数
    print("-------------------------------------------------")
    for i, m in enumerate(menu[str(key1)], 1):
        for item in m.keys():
            if item == key2:
                for i, item in enumerate(m[str(item)], 1):
                    print("    ", i, item)
    key = myinput()
    return key


def mymunici(key):
    # 输出4个直辖市的函数
    print("-------------------------------------------------")
    for i, item in enumerate(menu[str(key)], 1):
        print("    ", i, item)
    key = myinput()
    return key


def mysar(key):
    # 输出特别行政区的函数
    print("-------------------------------------------------")
    # for i, item in enumerate(menu[str(key)], 1):
    i = 1
    print("    ", i, menu[str(key)])
    key = myinput()
    return key


def exitorcontinue(key):
    # 判断用户键入的值，以便判断是否退出或返回上一级
    if key == 'q':
        sys.exit("感谢使用查询系统")
    elif key == 'b':
        return 0


# 导入yaml文件，并转换为字典格式
f = open('pro.yaml', 'r', encoding='utf-8')
menu = yaml.load(f)

# 定义直辖市列表，判断用户输入是否为直辖市
municipalities = ['北京市', '上海市', '重庆市', '天津市', ]

# 定义特别行政区
SAR = ['香港', '澳门', '台湾', '钓鱼岛', ]

# 定义在省级错误次数
n = 3

while True:
    if n == 0:  # 3次输入不正确直接退出系统
        sys.exit("感谢使用查询系统")

    print("-------------------------------------------------")
    for i, item in enumerate(menu.keys(), 1):    # 列出整个省级菜单
        print("    ", i, item)

    key1 = myinput()

    if key1 == 'q' or key1 == 'b':    # 判断此次键入的值是否为q,b
        sys.exit("感谢使用查询系统")

    if key1 not in menu.keys():    # 判断此次键入的值是否在所有可选的省级菜单中
        n -= 1
        print("-------------------------------------------------")
        print("你输入的省份不对，请重新输入")
        print("你还有%s次机会，否则将直接退出系统" %n)
        continue

    while True:
        if key1 in municipalities:    # 判断是否属于直辖市
            key2 = mymunici(key1)

            if exitorcontinue(key2) == 0:
                break
        elif key1 in SAR:    # 判断是否属于特别行政区
            key2 = mysar(key1)

            if exitorcontinue(key2) == 0:
                break
        else:   # 不属于直辖市
            key2 = mycity(key1)
            if exitorcontinue(key2) == 0:
                break

            while True:    # 查找第三级县菜单
                key3 = mycounty(key1, key2)

                if exitorcontinue(key3) == 0:
                    break
