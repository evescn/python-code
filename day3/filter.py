def myfunc(x):
    if x > 30:
        return True
    else:
        return False

a = [11, 22, 33]

new_a = filter(myfunc,a)

b = list(new_a)
print(b)