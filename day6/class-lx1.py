#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9 9:17
# @Author  : Evescn
# @Site    : 
# @File    : class-lx1.py
# @Software: PyCharm

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def kanchai(self):
        print("%s，%s岁，%s，上山去砍柴" %(self.name, self.age, self.gender))

    def qudongbei(self):
        print("%s，%s岁，%s，开车去东北" %(self.name, self.age, self.gender))

    def dabaojian(self):
        print("%s，%s岁，%s，最爱大保健" %(self.name, self.age, self.gender))


p1 = Person("小明", 10, "男")
p1.kanchai()
p1.qudongbei()
p1.dabaojian()

p2 = Person("老李", 90, "男")
p2.kanchai()
p2.qudongbei()
p2.dabaojian()