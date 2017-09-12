import collections

# obj = collections.Counter('aaabbccsdfsdfdfsdfsdf')
# obj = collections.Counter(['11', '22', '33', '22'])
# elements ==》 原生的值
# obj   ==》  处理后的值

# print(obj)
# ret1 = obj.most_common(2)
# print(ret1)

# for item in obj.elements():
#      print(item)
#
# for k,v in obj.items():
#     print(k,v)

# obj = collections.Counter(['11', '22', '33', '22'])
# print(obj)
# obj.update(['eric', '11', '11'])
# print(obj)
#
# obj.subtract(['eric', '11', '11', 'root'])
# print(obj)

dic = collections.OrderedDict()
# dic = dict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'
# dic['k4'] = None
# dic.setdefault('k5')
# for i in range(10)
# print(dic)

# # print(dic.keys())
#
# dic.move_to_end('k1')  # 启动某个keys到最后
#
# print(dic)

# dic.popitem()
#
# print(dic)

# dic.pop('k2')
# ret = dic.pop('k2')
# print(dic)
# print(ret)

# dic.update({'k1':'v111','k10':'v10'})
# print(dic)
#
# dic = collections.defaultdict(list)    # 设置dic的值类型为list
# dic['k1'].append('alex')
# print(dic)

# import collections
# # 创建类， defaultdict，坐标中会使用
# MytupleClass = collections.namedtuple('MytupleClass',['x', 'y', 'z'])
#
# obj = MytupleClass(11, 22, 33)
#
# # 获取MytupleClass的方法
# print(help(MytupleClass))
#
# print(obj.x)
# print(obj.y)
# print(obj.z)

# import collections
# d = collections.deque()
#
# d.append('1')
# d.appendleft('10')
# d.appendleft('a')
# d.appendleft('b')
# print(d)

# r = d.count('1')
# print(r)

# d.extend(['root', 'gm'])
# print(d)
#
# d.extendleft(['root', 'gm'])
# print(d)

# d.rotate(2)
# print(d)


import queue
# d = collections.deque()
q = queue.Queue(1)

print(q.empty())
print(q.full())
q.put('123')
print(q.full())
q.put('evescn')
print(dir(q))
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())