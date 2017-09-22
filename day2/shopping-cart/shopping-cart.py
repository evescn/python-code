#!/usr/bin/env python
# -*- conding:utf-8 -*-
# create a shopping cart system

# 20170921
# evescn

import sys


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
    i = 1
    with open(commodity, "r", encoding='utf-8') as f:
        for line in f:
            name, money, number = line.split()
            if i == 1:
                print("************************************")
            print("%-15s%-15s%-15s" %(name, money, number))
            if i == 1:
                print("************************************")
                i -= 1


def recharge():
    pass


def add_goods_shopping_cart():
    pass


def show_shopping_cart():
    pass


def show_bought_goods():
    pass


def remove_goods_from_bought():
    pass


def main():
    # 验证用户帐号和密码
    # login()

    # 显示当前商店内的所有商品
    show_goods()




if __name__ == "__main__":
    main()
