# f = open('test.log', 'w')
# f.write('evescn\n')
# f.write('evescn')
# f.close()
#
# f = open('test.log', 'r', encoding='utf-8')
# ret = f.read(10)
# f.close()
#
# print(ret)
#
# f = open('test.log', 'r', encoding='utf-8')
# ret = f.readline()
# f.close()
#
# print(ret)
#
# f = open('test.log', 'r', encoding='utf-8')
# ret = f.readlines()
# f.close()
#
# print(ret)
#
# f = open('test.log', 'r', encoding='utf-8')
# print(f.tell())
# ret = f.read(2)
# print(f.tell())
#
# f = open('test.log', 'r+', encoding='utf-8')
# f.seek(1)   #设置指针位置
# print(f.tell())   #查看当前指针位置
# ret = f.read(2)   #指定读取几个字符
# print(f.tell())

f = open('test.log', 'r+', encoding='utf-8')
f.seek(5)   #设置指针位置
# ret = f.read(2)
# print(ret)   #查看当前指针位置
f.truncate()   #把指针后的字符删除
# print(ret)
f.close()

# f = open('test.log', 'r', encoding='utf-8')
# ret = f.readlines()
# f.close()
#
# print(ret)


