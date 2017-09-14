#!/usr/bin/env python
# -*- conding:utf-8 -*-

# 无参数
# show():  --> show()

# # 一个参数
# def show(arg):
#     print(arg)
#
#
# show('evescn')
#
# # 两个参数
# def show(arg, xxx):
#     print(arg, xxx)
#
#
# show('evescn', 'gmkk')

# # 默认参数，必须写在最后
# def jiecheng(arg, n=2):
#     print(arg ** n)
#
#
# jiecheng(2)
# jiecheng(2,3)

# # 指定参数
# def show(a1,a2):
#     print(a1,a2)
#
#
# show(123,999)
# show(a2=123,a1=999)


# # 一个参数
# def show(arg):
#     print(arg)
#
# n = [11, 22, 33, 44]
# show(n)

# # 动态参数
# # 传入参数为列表  OK?
# def show(*arg):   # 把所有参数转为了元组
#     print(arg,type(arg))
#
# show(1,2,3,4,5,6,7,8)
#
# def show(**arg):  # 把所有参数转为了字典
#     print(arg,type(arg))
#
# show(n1=1,n2=2,n3=3,n4=4,)


# 规矩是先放变量，在放一个*的参数，在放**的参数
# def show(a1, *args, **kwargs):
#     print(a1)
#     print(args,type(args))
#     print(kwargs, type(kwargs))
#
# show(11,22,33,44,n1=99,n2=88,n3=77)

# def show(*args, **kwargs):
#     # print(a1)
#     print(args,type(args))
#     print(kwargs, type(kwargs))
#
# a1=[11,22,33,44]
# a2={'n1':99,'n2':88,'n3':77}
# show(a1,a2)
# show(*a1,**a2)

# s1 = "{0} to {1}"
# l = ['evescn','gmkk']
# ret1 = s1.format(*l)
# ret2 = s1.format('evescn','gmkk')
#
# print(ret1)
# print(ret2)
#
# s1 = "{name} to {acter}"
#
# l = {'name':'evescn', 'acter':'gmkk'}
# ret1 = s1.format(**l)
# ret2 = s1.format(name='evescn', acter='gmkk')
#
# print(ret1)
# print(ret2)


