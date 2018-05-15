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
    # 时间函数，计算费率

    # 验证用户帐号和密码
    username, id = module.login()

    # if

    # 显示当前商店内的所有商品
    module.show_goods()

    while True:
        # 输出显示信息
        key = module.show_info()
        print("*****************************")
        if key.lower() == 's':
            module.show_shopping_cart()
        elif key.lower() == 'e':
            module.edit_password(username)
        elif key.lower() == 'v':
            module.show_bought_goods()
        elif key.lower() == 'm':
            module.recharge(username)
        elif key.lower() == 'y':
            module.show_yue(username)
        elif key.lower() == 'b':
            module.goods_bought(username)
        elif key.lower() == 'g':
            module.show_goods()
        else:
            module.add_goods_shopping_cart(key)

# module.test()
if __name__ == "__main__":
    main()
