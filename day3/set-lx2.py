s1 = set([11,22,33])
s2 = set([22,44])

ret1 = s1.difference(s2)
ret2 = s1.symmetric_difference(s2)

print(ret1)
print(ret2)