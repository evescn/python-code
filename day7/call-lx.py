#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 22:07
# @Author  : Evescn
# @Site    : 
# @File    : call-lx.py
# @Software: PyCharm

class Foo:
    def __init__(self):
        print('__init__')
        self.n = 4
        # pass

    # def __new__(cls, *args, **kwargs):
    #     print('__new__')

    def __call__(self, *args, **kwargs):
        print('__call__')

    def test(self):
        print("__test__")

obj = Foo()  # 执行 __init__
# obj()  # 执行 __call__

# Foo()()

obj.test()
print(obj.__dict__)

print(type(Foo))