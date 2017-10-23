#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 16:08
# @Author  : Evescn
# @Site    : 
# @File    : xml模块.py
# @Software: PyCharm

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()
print(root.tag)

# 遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print("--->", i.tag, i.text)

# 只遍历year 节点
for node in root.iter("year"):
    print(node.tag, node.text)

