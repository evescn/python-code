l = [11, 22, 33, 44]

new_l = map(lambda x: x + 10, l)

a = list(new_l)
print(a)

# for i in a:
#     print(i)

def myadd(x):
    return x + 10

new_n = map(myadd, l)

b = list(new_n)
print(b)


