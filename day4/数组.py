#!/usr/bin/env python
# -*- conding-utf8 -*-

def xz(sz, n):
    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue
            else:
                t = sz[i][j]
                sz[i][j] = sz[j][i]
                sz[j][i] = t

    return sz

data = [[col for col in range(4)] for row in range(4)]
for i in data:
    print(i)
print("----------------------------")

b = xz(data, 4)
for i in b:
    print(i)
