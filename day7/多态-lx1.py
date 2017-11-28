#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 23:20
# @Author  : Evescn
# @Site    : 
# @File    : 多态-lx1.py
# @Software: PyCharm

# _*_coding:utf-8_*_


class Animal(object):
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    hobbie = "meat"

class Cat(Animal):
    def talk(self):
        print('%s: 喵喵喵!' % self.name)


class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)


def func(obj):  # 一个接口，多种形态
    obj.talk()


c1 = Cat('小晴')
d1 = Dog('李磊')

func(c1)
func(d1)
