#!/usr/bin/env python
# -*- conding:utf-8 -*-
# create a menu system

# 20170911
# evescn

import sys
import yaml

def myinput():
    print("输入q退出系统")
    print("输入b返回上一级菜单")
    key = input("请输入对应的字母进入下级菜单：")
    return key


def layers1(key):
    print("-------------------------------------------------")
    for i, item in enumerate(menu[str(key)], 1):
        print("    ", i, item)
    key = myinput()
    return key


def layers2(key1,key2):
    print("-------------------------------------------------")
    for i, item in enumerate(menu[str(key)][str(key)], 1):
        print("    ", i, item)
    key = myinput()
    return key


def layersz(key):
    print("-------------------------------------------------")
    # print(key)
    for i, item in enumerate(menu[str(key)], 1):
        print("    ", i, item)
    key = myinput()
    return key


def ifkey(key):
    if key == 'q':
        sys.exit("感谢使用查询系统")
    elif key == 'b':
        return 0


# menu = {
#     "bj":{"hd", "cy", "da"},
#     "sc":{"cd":["gx", "wh", "xd"], "zj":["fs", "xs", "zg"]},
#     "ty": []
# }

f = open('pro.yaml', 'r', encoding = 'utf-8')
menu = yaml.load(f)
# print(type(menu))
# print(menu)
# print(menu['0'])


n = 1
layers = 1

while layers != 0 and n < 4:
    print("-------------------------------------------------")
    for i,item in enumerate(menu.keys(),1):
        print("    ", i, item)

    key1 = myinput()
    print(key1)
    print('---------------------')

    if key1 == 'q' or key1 == 'b' or n ==3:
        sys.exit("感谢使用查询系统")

    if key1 not in menu.keys():
        print("-------------------------------------------------")
        print("你输入的省份不对，请重新输入")
        print("你还有%s次机会，否则将直接退出系统" %(3-n))
        n += 1
        continue

    while True:
        # key = int(key) - 1
        if key1 == '北京市':
            key2 = layersz(key1)

            if ifkey(key2) == 0:
                break

        else:
            key2 =layers1(key1)

            if ifkey(key2) == 0:
                break

            while True:
                key3 = layers2(key1,key2)

                if ifkey(key3 ) == 0:
                    break
