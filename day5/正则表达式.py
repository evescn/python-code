import re

# string = "192.168.2.22222"
# m = re.match("[0-9]{1,3}\.",string)
# m = re.match("([0-9]{1,3}\.){3}[0-9]{1,3}",string)
# m = re.match("(\d{1,3}\.){3}\d{1,3}",string)
#
# if m:
#     print(m.group())
#
# ip_addr = "inet 172.19.133.212 brd 172.19.143.255"
#
# m = re.search("(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}", ip_addr)

# m = re.search("

# print(m.group())
#
# if m:
#     print(m.group())
#
# string2 = "evescn"
# string3 = "Evescn"
#
# m = re.search("\w", string2)
# print(m.group())
#
# m = re.search("[a-z]", string3, flags=re.I)
# print(m.group())

# string4 = "evescn\ngmkk\n"
# m = re.search("^e.*$", string4, flags=re.M)
# m = re.search("^e.*$", string4)
# print(m)
# if m:
#     print(m.group())

# contactInfo = 'Evescn, ChengDu: 028-8888888'
# match = re.search(r'(\w+), (\w+): (\S+)', contactInfo)
# #分组   r按原生字符处理比如.
# print(match.group(1))
# print(match.group(2))
# print(match.group(3))

# match = re.search(r'(?P<name>\w+), (?P<addr>\w+): (?P<phone>\S+)', contactInfo)
#
# print(match.group('name'))
# print(match.group('addr'))
# print(match.group('phone'))

email = "evescn.gmkk@163.com   http://blog.evescn.com"

m = re.search(r"[0-9.a-z]{0,26}@[0-9.a-z]{0,20}.[0-9a-z]{0,8}", email)
print(m.group())