#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 22:26
# @Author  : Evescn
# @Site    : 
# @File    : mian4.py
# @Software: PyCharm

import re


def multi_or_divi(string):
    # 乘除法函数
    # 去掉括号
    calc_list = re.search("[^()]+", string)
    # 以乘除符号分割
    sub_calc_list = re.split("[*/]", calc_list.group())
    # 获取到字符串中的乘除符号
    sub_operator_list = re.findall("[*/]", calc_list.group())
    sub_res = None
    for index in range(len(sub_calc_list)):
        if sub_res:
            if sub_operator_list[index-1] == "*":
                sub_res *= float(sub_calc_list[index])
            else:
                sub_res /= float(sub_calc_list[index])
        else:
            sub_res = float(sub_calc_list[index])
    return float(sub_res)


def add_or_sub(string):
    # 加减法函数
    # 去掉括号
    calc_list = re.search("[^()]+", string)
    # 以加减符号分割
    sub_calc_list = re.split("[+-]", calc_list.group())
    # 获取到字符串中的加减符号
    sub_operator_list = re.findall("[+-]", calc_list.group())
    # 如果字符串已减号开头，需要特殊处理
    if re.match("[-+]", calc_list.group()):
        if sub_operator_list[0] == "-":
            sub_calc_list[1] = -float(sub_calc_list[1])
        # 对sub_operator_list和sub_calc_list进行字符串切割，或者到正确数据
        sub_operator_list = sub_operator_list[1:]
        sub_calc_list = sub_calc_list[1:]
        # 对字符串切割后，如何sub_calc_list为空，表示传过来的数为-X，直接返回sub_calc_list[0]即可，无需乘除运算
        if len(sub_operator_list) == 0:
            return sub_calc_list[0]
    sub_res = None
    for index in range(len(sub_calc_list)):
        if sub_res:
            if sub_operator_list[index-1] == "+":
                sub_res += float(sub_calc_list[index])
            else:
                sub_res -= float(sub_calc_list[index])
        else:
            sub_res = float(sub_calc_list[index])
    return float(sub_res)


def deal_minus_issue(ret):
    # 处理减法字符串
    # 创建一个新字符串用于返回处理后的字符串
    new_ret = []
    for index, item in enumerate(ret):
        if item.endswith("*") or item.endswith("/"):
            new_ret.append("%s-%s" %(ret[index], ret[index+1]))
        elif re.search("[*/]", ret[index]):
            new_ret.append(ret[index])
    return new_ret


def main():
    # 输入字符串
    a = '1 - 2 * ( (6-3 +(-5/5)*(9-2*3/3 + 7/3*7/4*12 +10 * 5/5 )) - (-4*3)/ (12-3*2) )'
    # a = '+(-40/5+3*(-12))'
    # 去空格
    a = a.replace(" ", "")
    # 设置循环退出的条件
    count = 2
    while True and count > 0:
        # 最内行括号
        calc_list = re.search(r'\([^()]+\)', a)
        if calc_list:
            # 如果能取到括号，把正则匹配结果赋值给calc_list_value
            calc_list_value = calc_list.group()
        else:
            # 如果不能取到括号，说明已经没有括号了，这只有加减乘除，对多只需要2次计算即可得出结果
            # 把a字符串赋值给calc_list_value
            count -= 1
            calc_list_value = a
        if "+" in calc_list_value or "-" in calc_list_value:
            if "*" in calc_list_value or "/" in calc_list_value:
                # 去掉括号以便以加减符号分割字符串
                calc_list1 = re.findall(r'[^()]+', calc_list_value)
                # 以加减符号去分割
                calc_list2 = re.split(r'[-+]', calc_list1[0])
                # 调用处理减法字符串函数，处理下*-或者/-这类问题
                calc_list2 = deal_minus_issue(calc_list2)
                # 返回后的calc_list列表只有包含乘除的式子
                for item in calc_list2:
                    # 对每一个乘除调用乘除函数
                    value = multi_or_divi(item)
                    # 把计算后的结果替换掉原来的值
                    a = a.replace(item, str(value))
                    # 处理下字符串中出现的++或+-问题
                    a = a.replace("+-", "-")
                    a = a.replace("--", "+")
            else:
                # 式子中没有乘除符号，那就只有加减符号，调用加减函数
                value = add_or_sub(calc_list_value)
                # 把计算后的结果替换掉原来的值
                a = a.replace(calc_list_value, str(value))
                # 处理下字符串中出现的++或+-问题
                a = a.replace("+-", "-")
                a = a.replace("--", "+")
        else:
            if "*" in calc_list_value or "/" in calc_list_value:
                # 式子中没有加减符号，那就只有乘除符号，调用处理减法字符串函数，处理下*-或者/-这类问题
                value = multi_or_divi(calc_list_value)
                # 把计算后的结果替换掉原来的值
                a = a.replace(calc_list_value, str(value))
                # 处理下字符串中出现的++或+-问题
                a = a.replace("+-", "-")
                a = a.replace("--", "+")
        print("a:", a)

if __name__ == '__main__':
    main()