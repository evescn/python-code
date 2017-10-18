#/usr/bin/eve python
# -*- coding:utf-8 -*-

data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]

# for index,i in enumerate(data[:-1]):
#     if i > data[index+1]:
#         data[index+1], data[index] = i, data[index+1]

l = len(data)
print(l)
for i in range(l):
    for j in range(l-1-i):
        if data[j] > data[j+1]:
            tmp = data[j]
            data[j] = data[j+1]
            data[j+1] = tmp
            # data[i], data[j] = data[j], data[i]
    print(data)
print(data)