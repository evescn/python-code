#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 22:15
# @Author  : Evescn
# @Site    : 
# @File    : exception-lx.py
# @Software: PyCharm

while True:
    num1 = input("num1:")
    num2 = input("num2:")
    a = range(10)
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        # a[11]
    except IndentationError as e:
        print("IndentationError:", e)
    except ValueError as e:
        print("value err:", e)
    except IndexError as e:
        print("Index Error:", e)
    # except Exception, e:    # 2.7版本
    except Exception as e:
        print("出现异常，信息如下：")
        print(e)