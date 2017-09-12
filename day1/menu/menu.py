#!/usr/bin/env python
# -*- conding:utf-8 -*-
# create a menu system

# 20170911
# evescn

menu = {
    "bj":{"hd", "cy", "da"},
    "sc":{"cd":["gx", "wh", "xd"], "zj":["fs", "xs", "zg"]},
    "ty": []
}

layers = 1

while layers != 0:

    i = 0
    for item in menu.keys():
        print(i, item)
        i += 1

    print("输入q退出系统")
    print("输入b返回上一级菜单")
    input("请输入对应的数字进入下级菜单：")
    layers -= 1

