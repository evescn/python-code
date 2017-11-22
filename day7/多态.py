#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 23:08
# @Author  : Evescn
# @Site    : 
# @File    : 多态.py
# @Software: PyCharm

# _*_coding:utf-8_*_


class Animal(object):
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        # print('%s: 喵喵喵!' % self.name)
        return ('喵喵喵!')


class Dog(Animal):
    def talk(self):
        # print('%s: 汪！汪！汪！' % self.name)
        return ('汪！汪！汪！')


animals = [Cat("Evescn"),
           Dog("Gmkk")]

for animal in animals:
    print(animal.name + "：" + animal.talk())