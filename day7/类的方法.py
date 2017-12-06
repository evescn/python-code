#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 22:33
# @Author  : Evescn
# @Site    : 
# @File    : 类的方法.py
# @Software: PyCharm

class Animal(object):
    def __init__(self, name):  # Constructor of the class
        self.name = name
        # self.num = None
        self.__num = None   # 私有变量

    @classmethod   # 类方法，不能访问实例变量
    def talk(self):  # Abstract method, defined by convention only
        # raise NotImplementedError("Subclass must implement abstract method")
        print("%s is talking..." %self.name)

    @staticmethod  # 静态方法，不能访问类变量和实例变量，把它作为类的工具箱
    def walk():
        print("Test is walking...")

    @property     # 把方法变成属性
    def habit(self):
        # self.num = num
        # print("%s habit shuijiao" %self.__num)
        return self.__num

    @habit.setter     # 把方法变成属性，并且可以赋值
    def habit(self, num):
        self.__num = num
        print("%s habit shuijiao" %self.__num)

    @habit.deleter     # 把方法变成属性，并且可以赋值
    def habit(self):
        # self.num = num
        print("del habit shuijiao")
        del self.__num

    hobbie = "meat"


# print(Animal.hobbie)
# Animal.hobbie
# Animal.talk()

d = Animal("evescn")
# d.talk()
# d.walk()
# d.habit()
print(d.habit)
d.habit = 3
d.__num = 6
print("OUT:", d.__num)
print("OUT:", d._Animal__num)   # 特例访问私有变量
# del d.habit
# d.habit = 3
print(d.habit)
# print(d.num)


# class Cat(Animal):
#     def talk(self):
#         print('%s: 喵喵喵!' % self.name)
#
#
# class Dog(Animal):
#     def talk(self):
#         print('%s: 汪！汪！汪！' % self.name)
#
#
# def func(obj):  # 一个接口，多种形态
#     obj.talk()
#
#
# c1 = Cat('小晴')
# d1 = Dog('李磊')
#
# func(c1)
# func(d1)