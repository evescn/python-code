#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 15:56
# @Author  : Evescn
# @Site    : 
# @File    : mysqlAPI.py
# @Software: PyCharm

import pymysql

conn = pymysql.connect(host='172.20.3.220', user='root', password='123456', db='evescn')

cur = conn.cursor()

# 插入语句
# reCount = cur.execute('insert into students(name, sex, age) values(%s,%s,%s)', ('evescn', 'man', 22))
# conn.commit()

# 插入多条
data = [
    ('eve1', 'man', 22),
    ('eve2', 'man', 22),
    ('eve3', 'man', 22),
]
reCount = cur.executemany('insert into students(name, sex, age) values(%s,%s,%s)', data)
conn.commit()

# 删除语句
# reCount = cur.execute('delete from students where id=3')
# conn.commit()

# 修改语句
# reCount = cur.execute('update students set name="eve" where id=1')
# conn.commit()

# 查询数据
# reCount = cur.execute('select * from students')

# print(cur.fetchmany(2)) # 指定多少条
# print(cur.fetchone())
# print(cur.fetchall())

# 回滚
# print(cur.fetchall())
# reCount = cur.execute('insert into students(name, sex, age) values(%s,%s,%s)', ('evescn', 'man', 22))
# reCount = cur.execute('insert into students(name, sex, age) values(%s,%s,%s)', ('evescn', 'man', 22))
# reCount = cur.execute('insert into students(name, sex, age) values(%s,%s,%s)', ('evescn', 'man', 22))
#
# reCount = cur.execute('select * from students')
# print(cur.fetchall())
# conn.rollback()
# print(cur.fetchmany())
# conn.commit()



cur.close()
conn.close()

print(reCount)

