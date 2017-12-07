#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 22:51
# @Author  : Evescn
# @Site    : 
# @File    : multi_inhertance.py
# @Software: PyCharm

class A:
    n = 'A'
    def f2(self):
        print("from A")

class B(A):
    n = 'B'

    def f1(self):
        print("from B")
    def f2(self):
        print("from B")

class C(A):
    n = 'C'

    def f2(self):
        print("from C")


# 经典类继承是深度优先，新式类继承是广度优先

class D(B,C):    # 继承遵循广度有优先，先继承B的方法，B没有的方法才去继承C的方法，最后才去继承A的方法
    # Test class
    '''Test2 class'''
    pass


d = D()
d.f1()
d.f2()

print(d.__doc__)   # 输出类注释
print(d.__module__)   # 输出类注释
