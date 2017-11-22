#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 21:57
# @Author  : Evescn
# @Site    : 
# @File    : main.py
# @Software: PyCharm

# import pickle
import sys
import random


class Person(object):
    def __init__(self, name, gender, intimacy):
        self.name = name
        self.gender = gender
        self.intimacy = intimacy

    def Add_Intimacy(self, intimacy_num):
        num = int(intimacy_num)
        self.intimacy = int(self.intimacy) + num


class Man(Person):
    def __init__(self, name, gender, intimacy):
        super(Man, self).__init__(name, gender, intimacy)


    def SongHua(self):
        print("送出了一朵花，亲密度增加5点。")
        return 5


    def DaShui(self):
        print("打了一次水，亲密度增加5点。")
        return 5


    def ZaoCan(self):
        print("买了一次早餐，亲密度增加10点。")
        return 10


    def MaRen(self):
        print("骂了女朋友，亲密度\033[31m减少\033[0m15点。")
        return -15


class Woman(Person):
    def __init__(self, name, gender, intimacy):
        super(Woman, self).__init__(name, gender, intimacy)


    def SongWerJing(self):
        print("送了一个围巾，亲密度增加20点。")
        return 10


    def QinQin(self):
        print("亲了一下，亲密度增加40点。")
        return 40


    def ZaoCan(self):
        print("买了一次早餐，亲密度增加10点。")
        return 20


    def ShenQi(self):
        print("生气了，亲密度减少10点。")
        return -10


def ShowInfo(key):
    if key == "begin":
        info = '''
====================================
    1、进入游戏    2、退出游戏
====================================
        '''
        print("\033[1;;33m%s\033[0m" %info)
        return input("请输入你的选择：")
    elif key == "error":
        info = '''
=====================================================
        你的输入不正确，请重新输入
=====================================================
             '''
        print("\033[1;;33m%s\033[0m" % info)
        # return input("请输入角色名字：")
    elif key == "role":
        info = '''
=====================================================
                请选择你的游戏角色
evescn：男性角色    hlr：女性角色    q：退出游戏
=====================================================
         '''
        print("\033[1;;33m%s\033[0m" % info)
        return input("请输入角色名字：")
    elif key == "way":
        info = '''
=====================================================
                请选择游戏方式
1、自动游戏    2、手动游戏    q、退出游戏
=====================================================
        '''
        print("\033[1;;33m%s\033[0m" % info)
        return input("请选择游戏方式：")
    elif key == "manway":
        info = '''
=====================================================
                 请选择游戏方式
1、送一朵花    
2、打一次水
3、买一次早餐
4、骂女朋友  
q、退出游戏
=====================================================
        '''
        print("\033[1;;33m%s\033[0m" % info)
        return input("请选择你的行为：")
    elif key == "womanway":
        info = '''
=====================================================
                 请选择游戏方式
1、送一个围巾    
2、亲一下
3、买一次早餐
4、生气了  
q、退出游戏
=====================================================
        '''
        print("\033[1;;33m%s\033[0m" % info)
        return input("请选择你的行为：")

def Mangame(num):
    if num == 1:
        ret = evescn.SongHua()
        hlr.Add_Intimacy(ret)
    elif num == 2:
        ret = evescn.DaShui()
        hlr.Add_Intimacy(ret)
    elif num == 3:
        ret = evescn.ZaoCan()
        hlr.Add_Intimacy(ret)
    elif num == 4:
        ret = evescn.MaRen()
        hlr.Add_Intimacy(ret)


def Womangame(num):
    if num == 1:
        ret = hlr.SongWerJing()
        evescn.Add_Intimacy(ret)
    elif num == 2:
        ret = hlr.QinQin()
        evescn.Add_Intimacy(ret)
    elif num == 3:
        ret = hlr.SongWerJing()
        evescn.Add_Intimacy(ret)
    elif num == 4:
        ret = hlr.ZaoCan()
        evescn.Add_Intimacy(ret)


def autogame(name):
    day = 1
    while int(hlr.intimacy) > 0 and int(hlr.intimacy) < 100 and int(evescn.intimacy) > 0 and int(evescn.intimacy) < 100:
        num = random.randint(1, 4)
        print("第【%s】天" %day, end="")
        day += 1
        if name == "evescn":
            Mangame(num)
        else:
            Womangame(num)
        print()
    else:
        if int(hlr.intimacy) <= 0 or int(evescn.intimacy) <= 0:
            print("\033[1;;31m恋爱失败！\033[0m")
            hlr.intimacy = 10
            evescn.intimacy = 10
        else:
            print("\033[1;;31m恋爱成功！\033[0m")
            hlr.intimacy = 10
            evescn.intimacy = 10


def game(name):
    day = 1
    while int(hlr.intimacy) > 0 and int(hlr.intimacy) < 100 and int(evescn.intimacy) > 0 and int(evescn.intimacy) < 100:
        if name == "evescn":
            num = ShowInfo("manway")
            num = int(num)
            if num < 1 or num > 4:
                ShowInfo("error")
            else:
                print("第【%s】天" % day, end="")
                day += 1
                Mangame(int(num))
                print()
        else:
            num = ShowInfo("womanway")
            num = int(num)
            if num < 1 or num > 4:
                ShowInfo("error")
            else:
                print("第【%s】天" % day, end="")
                day += 1
                Womangame(int(num))
                print()
    else:
        if int(hlr.intimacy) <= 0 or int(evescn.intimacy) <= 0:
            print("\033[1;;31m恋爱失败！\033[0m")
            hlr.intimacy = 10
            evescn.intimacy = 10
        else:
            print("\033[1;;31m恋爱成功！\033[0m")
            hlr.intimacy = 10
            evescn.intimacy = 10


def main():
    ret = ShowInfo("begin")
    while True:
        if ret == "2":
            sys.exit("欢迎下次再来！")
        elif ret == "1":
            game_role = ShowInfo("role")
            if game_role == "q":
                sys.exit("欢迎下次再来！")

            flag = True
            while flag:
                if game_role == "evescn" or game_role == "hlr":
                    flag = False
                else:
                    # print()
                    # print("\033[1;;35m====================================================\033[0m")
                    # print("输入的角色名不正确，请重新输入名字")
                    # print("\033[1;;35m====================================================\033[0m")
                    ShowInfo("error")
                    game_role = ShowInfo("role")

            game_way = ShowInfo("way")
            if game_way == "q":
                sys.exit("欢迎下次再来！")
            elif game_way == "1":
                autogame(game_role)
            elif game_way == "2":
                game(game_role)
            else:
                print()
                print("\033[1;;35m====================================================\033[0m")
                print("\033[31m你的游戏方式不正确\033[0m")
                print("\033[1;;35m====================================================\033[0m")

        else:
            # print()
            # print("\033[1;;35m====================================================\033[0m")
            # print("\033[32m不知道你的选择是什么，请重新输入\033[0m")
            # print("\033[1;;35m====================================================\033[0m")
            ShowInfo("error")
            ret = ShowInfo("begin")


if __name__ == '__main__':
    evescn = Man("evescn", "M", "10")
    hlr = Woman("hlr", "F", "10")
    main()

