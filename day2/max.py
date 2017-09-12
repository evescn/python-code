#!/usr/bin/env python

def max_number(m, n):
    if m > n:
        return m
    else:
        return n


a = 3
b = 44
c = 5

x = max_number(a, b)
y = max_number(x, c)

print(y)

