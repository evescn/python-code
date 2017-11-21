#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 21:57
# @Author  : Evescn
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import pickle


class Person(object):
    def __init__(self, name, password, gender, intimacy):
        self.name = name
        self.password = password
        self.gender = gender
        self.intimacy = intimacy

    def Add_Intimacy(self, intimacy_num):
        num = int(intimacy_num)
        self.intimacy = int(self.intimacy) + num


class Man(Person):
    def __init__(self, name, password, gender, intimacy):
        super(Man, self).__init__(name, password, gender, intimacy)

    def Main(self, info):
        f = open("man.log", "wb")
        pickle.dump(info, f)
        f.close()

    def ReMain(self, info):
        f = open("man.log", "rb", encoding="utf-8")
        data = pickle.loads(f)
        f.close()
        # for line in f:
        #     print(line)

    def SongHua(self):
        print("送出了一朵花")
        # self.Add_Intimacy(10)
        hlr.Main("送出了一朵花")

    def DaShui(self):
        print("打了一次水")
        # self.Add_Intimacy(10)
        hlr.Main("打了一次水")

    def ZaoCan(self):
        print("买了一次早餐")
        # self.Add_Intimacy(10)
        hlr.Main("买了一次早餐")

    def MaRen(self):
        print("骂了女朋友")
        # self.Add_Intimacy(-10)
        hlr.Main("骂了女朋友")

class Woman(Person):
    def __init__(self, name, password, gender, intimacy):
        super(Woman, self).__init__(name, password, gender, intimacy)

    def Main(self, info):
        f = open("woman.log", "wb")
        pickle.dump(info, f)
        f.close()

    def ReMain(self, info):
        f = open("woman.log", "rb")
        data = pickle.loads(f)
        f.close()
        print(data)
        # print.print(data)
        for line in data:
            print(line)

    def SongWerJing(self):
        print("送了一个围巾，亲密度增加10点。")
        # self.Add_Intimacy(10)
        evescn.Main("送了一个围巾")

    def QinQin(self):
        print("亲了一下，亲密度增加10点。")
        # self.Add_Intimacy(10)
        evescn.Main("亲了一下")

    def ZaoCan(self):
        print("买了一次早餐，亲密度增加10点。")
        # self.Add_Intimacy(10)
        evescn.Main("买了一次早餐")

    def ShenQi(self):
        print("生气了，亲密度减少10点。")
        # self.Add_Intimacy(-10)
        evescn.Main("生气了")

evescn = Man("evescn", "evescn", "M", "0")
hlr = Woman("hlr", "hlr", "F", "0")

evescn.ZaoCan()
print(evescn.intimacy)
evescn.DaShui()
print(evescn.intimacy)
evescn.MaRen()
print(evescn.intimacy)
print(hlr.Main)

hlr.ZaoCan()
print(hlr.intimacy)
hlr.QinQin()
print(hlr.intimacy)
hlr.ShenQi()
print(hlr.intimacy)