#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 9:28
# @Author  : Evescn
# @Site    : 
# @File    : main.py.py
# @Software: PyCharm

import sys
import os
import yaml
from prettytable import PrettyTable

from modules import module


def main():
    # 验证用户帐号和密码
    username = module.login

    # 显示当前商店内的所有商品
    module.show_goods()

    while True:
        # 输出显示信息
        key = show_info()
        print("*****************************")
        if key.lower() == 's':
            show_shopping_cart()
        elif key.lower() == 'e':
            edit_password(username)
        elif key.lower() == 'v':
            show_bought_goods()
        elif key.lower() == 'm':
            recharge(username)
        elif key.lower() == 'y':
            show_yue(username)
        elif key.lower() == 'b':
            goods_bought(username)
        elif key.lower() == 'g':
            show_goods()
        else:
            add_goods_shopping_cart(key)

# module.test()
if __name__ == "__main__":

    main()
