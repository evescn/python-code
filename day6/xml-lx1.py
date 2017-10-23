#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 16:23
# @Author  : Evescn
# @Site    : 
# @File    : xml-lx1.py
# @Software: PyCharm

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()

# 修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updated", "yes")
#     # break
#
# tree.write("xmltest.xml")

# for node in root.iter('year'):
#     name = str(node.find('name').text)
#     if name == "Panama":
#         new_year = int(node.text) + 10
#         node.text = str(new_year)
#         node.set("updated", "yes")
#
# tree.write("xmltest.xml")

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')