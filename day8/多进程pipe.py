#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 21:31
# @Author  : Evescn
# @Site    : 
# @File    : 多进程pipe.py
# @Software: PyCharm

from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()

    p2 = Process(target=f, args=(child_conn,))
    p2.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p2.join()