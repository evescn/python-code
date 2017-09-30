#!/usr/bin/env python
# -*- conding:utf-8 -*-
# create a shopping cart system

# 20170921
# evescn

import sys
import os
import yaml
from prettytable import PrettyTable


def login():
    # 验证用户帐号和密码函数
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
                    return name
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


def show_shopping_cart():
    # 显示购物车商品函数
    open_shop_cart()


def show_bought_goods():
    # 显示已购买商品函数
    open_bought()


def show_yue(username):
    # 显示帐号的金额
    money = "money.txt"
    x = PrettyTable(["用户", "余额"])
    x.align["用户"] = "l"  # 以name字段左对齐
    x.align["余额"] = "r"  # 以name字段右对齐
    x.padding_width = 1  # 填充宽度
    with open(money, "r", encoding='utf-8') as f:
        for line in f:
            name, money = line.split()
            if name == username:
                x.add_row([name, money])
        print(x)


def show_info():
    # 显示信息函数
    print("*****************************")
    print("修改密码，请输入E：")
    print("查看购物车，请输入S：")
    print("查看已购买商品函数，请输入V：")
    print("充值，请输入M：")
    print("查询余额，请输入Y：")
    print("购买商品，请输入B：")
    print("查看商品数量和价格，请输入G：")
    print("添加商品到购物车，请输入商品名称：")
    print("*****************************")
    return input("请输入你的选择：")


def recharge(username):
    # 充值函数
    key = username
    n = input("请输入充值金额:")
    filename = "money.txt"
    edit_file_data(filename, username, n, '+')
    return


def add_goods_shopping_cart(key):
    # 添加商品到购物车函数
    n = input("请输入购买数量：")
    file1 = "commodity.txt"
    file2 = "shop-cart.txt"
    ret = edit_file_data(file1, key, n, '-')
    if int(ret) == 1:
        print("*****************************")
        print("商品数量不足，请重新选择")
        return
    else:
        edit_file_data(file2, key, n, '+')


def goods_bought(username):
    # 从商品购买函数
    while True:
        show_shopping_cart()
        q = input("输入q返回上级菜单,输入其他键继续：")
        if q.lower() == 'q':
            return
        # else:
        key = input("请输入购买商品名称：")
        n = input("请输入购买数量：")
        file1 = "money.txt"
        file2 = "shop-cart.txt"
        file3 = "bought.txt"
        with open("commodity.txt", "r", encoding='utf-8') as f1:
            for line in f1:
                shop = line.split()
                if str(shop[0]) == str(key):
                    value = shop[2]
        sum_value = int(n) * int(value)
        with open(file1, "r", encoding='utf-8') as f1:
            for line in f1:
                shop = line.split()
                if str(shop[0]) == str(username):
                    value = shop[1]
        if int(sum_value) > int(value):
            print("*****************************")
            print("余额不足请充值：")
            print("*****************************")
            return recharge(username)

        ret = edit_file_data(file2, key, n, '-')
        if int(ret) == 1:
            print("*****************************")
            print("购物车中没有这么多商品，请重新选择")
            print("*****************************")
            continue
        else:
            edit_file_data(file1, username, sum_value, '-')
            edit_file_data(file3, key, n, '+')


def edit_password(username):
    # 修改帐号密码函数
    passwd1 = input("请输入你的新密码：")
    passwd2 = input("请再次确认你的密码：")
    if passwd1 != passwd2:
        print("*****************************")
        print("你2次输入的密码不一致,请重新输入")
        print("*****************************")
        return edit_password(username)
    else:
        file1 = "password.txt"
        file2 = "tmp.txt"
        with open(file1, "r", encoding='utf-8') as f1:
            with open(file2, "w", encoding='utf-8') as f2:
                for line in f1:
                    shop = line.split()
                    if str(shop[0]) == str(username):
                        shop[1] = str(passwd1)
                        dat_out = " ".join(shop)
                        f2.write(dat_out + "\n")
                    else:
                        dat_out = " ".join(shop)
                        f2.write(dat_out + "\n")
        move_filename(file1)
        print("*****************************")
        print("密码修改成功！")
        print("*****************************")


def open_shop_cart():
    x = PrettyTable(["商品名称", "数量"])
    x.align["商品名称"] = "l"  # 以name字段左对齐
    # x.align["价格"] = "r"  # 以name字段右对齐
    x.align["数量"] = "r"  # 以name字段右对齐
    x.padding_width = 1  # 填充宽度
    with open("shop-cart.txt", "r", encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            x.add_row([name, number])
        print("*****************************")
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
    pass


def open_bought():
    x = PrettyTable(["商品名称", "数量"])
    x.align["商品名称"] = "l"  # 以name字段左对齐
    x.align["数量"] = "r"  # 以name字段右对齐
    x.padding_width = 1  # 填充宽度
    with open("bought.txt", "r", encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            x.add_row([name, number])
        print(x)


def move_filename(filename):
    # 重命名文件名函数
    for file in os.listdir('.'):  # os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
        if file == filename:
            os.remove(file)
    for file in os.listdir('.'):
        if file == "tmp.txt":
            new_name = filename
            os.rename(file, new_name)
            return


def edit_file_data(filename, key, n, operator):
    # 修改文件数据函数
    file2 = "tmp.txt"
    sign = 0
    if operator == '+':
        with open(filename, "r", encoding='utf-8') as f1:
            with open(file2, "w", encoding='utf-8') as f2:
                for line in f1:
                    shop = line.split()
                    if str(shop[0]) == str(key):
                        sign = 1
                        shop[1] = str(int(shop[1]) + int(n))
                        dat_out = " ".join(shop)
                        f2.write(dat_out + "\n")
                    else:
                        dat_out = " ".join(shop)
                        f2.write(dat_out + "\n")
                if sign == 0:
                    shop = [key, str(n)]
                    dat_out = " ".join(shop)
                    f2.write(dat_out + "\n")
    elif operator == '-':
        with open(filename, "r", encoding='utf-8') as f1:
            with open(file2, "w", encoding='utf-8') as f2:
                for line in f1:
                    shop = line.split()
                    if str(shop[0]) == str(key):
                        if int(shop[1]) < int(n):
                            return 1
                        else:
                            shop[1] = str(int(shop[1]) - int(n))
                            dat_out = " ".join(shop)
                            f2.write(dat_out + "\n")
                    else:
                        dat_out = " ".join(shop)
                        f2.write(dat_out + "\n")

    move_filename(filename)
    return 0


def main():
    # 验证用户帐号和密码
    username = login()

    # 显示当前商店内的所有商品
    show_goods()

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


if __name__ == "__main__":
    main()
