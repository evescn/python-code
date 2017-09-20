
name = iter(['evescn', 'root', 'gmkk'])

print(name)
print(name.__next__())
print(name.__next__())
print(name.__next__())


# 如何迭代的读入文件
f =  open("__init.py")
f.read()
f.readlines()

for line in f:
    print(line)


