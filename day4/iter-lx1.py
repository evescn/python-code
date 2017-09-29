
name = iter(['evescn', 'root', 'gmkk'])

print(name)
print(name.__next__())
print(name.__next__())
print(name.__next__())

for i in name:
    print(i)

print("-------------------")
# 如何迭代的读入文件
f = open("test.txt")
# f.read()
# f.readlines()

for line in f:
    print(line.strip())


