#!/usr/bin/env python
# -*- conding:utf-8 -*-
# create a shopping cart system

# 20170921
# evescn

import sys
from prettytable import PrettyTable
import yaml

def login():
    # 验证用户帐号和密码
    global name
    lock = "lock.txt"
    loginfile = "password.txt"
    login_info = 0
    i = 0

    while i < 3 and login_info == 0:
        name = input("Please input your name: ")

        with open(lock, "r") as f:
            for line in f:
                # if name in line:
                if name == line.strip():
                    sys.exit('\033[32:1m用户 %s 已经被锁定\033[0m' % name)

        password = input("Please input password: ")

        with open(loginfile, "r") as f:
            for line in f:
                user_file, pass_file = line.split()
                if user_file == name and pass_file == password:
                    print("Bingo!")
                    login_info = 1
                    break
            else:
                print("You name or password is error!")
                i += 1

    else:
        if i == 3 and login_info == 0:
            f = open(lock, "a")
            f.write(name + "\n")
            f.close()
            print('\033[32:1m用户 %s 已经被锁定\033[0m' % name)


def show_goods():
    # 显示当前商店内的所有商品
    commodity = "commodity.txt"
    x = PrettyTable(["商品名称", "价格", "数量"])
    x.align["商品名称"] = "l"  # 以name字段左对齐
    x.align["价格"] = "r"  # 以name字段右对齐
    x.align["数量"] = "r"  # 以name字段右对齐
    x.padding_width = 1  # 填充宽度
    with open(commodity, "r", encoding='utf-8') as f:
        for line in f:
            name, money, number = line.split()
            x.add_row([name, money, number])

        print(x)



def recharge():
    # 充值函数
    name = input("请输入充值帐号：")
    money = input("请输入充值金额:")
    # money_dict = {}
    with open("money.yaml", "r", encoding='utf-8') as f:
        money_dict = yaml.load(f)

        money_dict[str(name)] = int(money_dict[str(name)]) + int(money)
        print(money_dict)

    with open("money.yaml", "wt", encoding='utf-8') as f:
        f.write(yaml.dump(money_dict))


def add_goods_shopping_cart():
    # 添加商品到购物车函数
    pass


def show_shopping_cart():
    # 显示购物车商品函数
    # pass
    open_shop_cart()

def show_bought_goods():
    # 显示已购买商品函数
    pass


def remove_goods_from_bought():
    # 从商品中移除已购买的
    pass


def show_info():
    print("*****************************")
    print("查看购物车，请输入S：")
    print("充值，请输入M：")
    print("查看商品数量和价格，请输入G：")
    print("添加商品到购物车，请输入商品名称：")
    print("购买商品，请输入B：")
    print("*****************************")
    return input("请输入你的选择：")


def open_password():
    pass

def open_shop_cart():
    x = PrettyTable(["商品名称", "价格", "数量"])
    x.align["商品名称"] = "l"  # 以name字段左对齐
    x.align["价格"] = "r"  # 以name字段右对齐
    x.align["数量"] = "r"  # 以name字段右对齐
    x.padding_width = 1  # 填充宽度
    with open("shop-cart.txt", "r", encoding='utf-8') as f:
        for line in f:
            name, money, number = line.split()
            x.add_row([name, money, number])
        print(x)


def open_commodity():
    x = PrettyTable(["商品名称", "价格", "数量"])
    x.align["商品名称"] = "l"  # 以name字段左对齐
    x.align["价格"] = "r"  # 以name字段右对齐
    x.align["数量"] = "r"  # 以name字段右对齐
    x.padding_width = 1  # 填充宽度
    with open("commodity.txt", "r", encoding='utf-8') as f:
        for line in f:
            name, money, number = line.split()
            x.add_row([name, money, number])
        print(x)


def open_money(name, money):
    money_sum = money
    with open("money.yaml", "r", encoding='utf-8') as f:
        for line in f:
            name_money, money_money = line.split()
            if name == name_money:
                money_sum = money_money + money

    # if money_sum != money:
        # with open

def main():
    # 验证用户帐号和密码
    # login()

    # 显示当前商店内的所有商品
    show_goods()

    while True:
        # 输出显示信息
        key = show_info()
        print("*****************************")
        if key.lower() == 's':
            show_shopping_cart()
        elif key.lower() == 'm':
            recharge()
        elif key.lower() == 'b':
            add_goods_shopping_cart()
        elif key.lower() == 'g':
            show_goods()
        else:
            add_goods_shopping_cart()







if __name__ == "__main__":
    main()
