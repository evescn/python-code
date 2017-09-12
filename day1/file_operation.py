"""
f = open("test.log", "w")

f.write("This is the first line\n")
f.write("This is the 2 line\n")
f.write("This is the 3 line\n")
f.write("This is the 4 line\n")

f.close()
"""

# """
f = open("test.log", "r")
# print(f.read())
# print(f.readline())
for i in f.readlines():
    a, b = i.split()
    print('a is ', a)
    print()
    print('b is ', b)
    if "3" in i:
        print("This is the thire line")
    else:
        print(i.strip())

f.close()
# """

"""
f = open("test.log", "a")
f.write("root\n")
f.write("gm\n")

f.close()
"""

"""
f = open("test.log", "w+")
f.write("new line\n")
print(f.readline())
f.close()
"""