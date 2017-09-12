s1 = set()
s1.add('evescn')
#print(s1)
s1.add('evescn')
#print(s1)
# 访问速度块
# 天生解决了重复问题

s2 = set(['alex', 'eric', 'tony', 'alex'])
# print(s2)
s2.difference(['alex', 'eric'])
# print(s2)

s3 = s2.difference(['alex', 'eric'])
# print(s3)

"""
s4 = s2.difference_update(['alex', 'eric'])
print(s2)
print(s4)

ret = s2.pop()
print(s2)
print(ret)
"""

old_dict = {
	"#1":{"hostname": 'c1', 'cpu_count': 2, 'mem_capicit': 80},
	"#2":{"hostname": 'c1', 'cpu_count': 2, 'mem_capicit': 80},
	"#3":{"hostname": 'c1', 'cpu_count': 2, 'mem_capicit': 80}
}

# cmdb 新汇报的数据
new_dict = {
	"#1":{"hostname": 'c1', 'cpu_count': 2, 'mem_capicit': 70},
	"#3":{"hostname": 'c1', 'cpu_count': 2, 'mem_capicit': 80},
	"#4":{"hostname": 'c1', 'cpu_count': 2, 'mem_capicit': 80}
}

old = set(old_dict.keys())
new = set(new_dict.keys())

print(old)
print(new)

update_set = old.intersection(new)  #要更新的集合
delete_set = old.difference(new)    #要删除的集合
add_set = new.difference(old)       #要添加的集合

print(update_set)
print(delete_set)
print(add_set)