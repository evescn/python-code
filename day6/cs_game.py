#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 22:13
# @Author  : Evescn
# @Site    : 
# @File    : cs_game.py
# @Software: PyCharm

class Role(object):
    ac = None  # 作用：可以知道游戏一共有多少角色，公共性的数据
    def __init__(self, name, role, weapon, life_value):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        # Role.ac +=1

    def buy_weapon(self, weapon):
        print("%s is buying [%s]" %(self.name, weapon))
        self.weapon = weapon
        print(self.ac)


p1 = Role("Evescn", "Police", "B11", 90)
# Role(p1, "Evescn", "Police", "B11", 90)
t1 = Role("Gmkk", "Terrorist", "B11", 100)

print("P1.name =", p1.name)
print("T1.name =", t1.name)

print("P1:", p1.weapon)
print("T1:", t1.weapon)

p1.buy_weapon("AK47")
t1.buy_weapon("B41")

p1.ac = "China Brand"
t1.ac = "USA Brand"
print("P1:", p1.weapon, p1.ac)
print("T1:", t1.weapon, t1.ac)