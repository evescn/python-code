import re

# string = "192.168.2.22222"
# m = re.match("[0-9]{1,3}\.",string)
# m = re.match("([0-9]{1,3}\.){3}[0-9]{1,3}",string)
# m = re.match("(\d{1,3}\.){3}\d{1,3}",string)
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

contactInfo = 'Oldboy School, Beijing Changping Shahe: 010-8343245'
match = re.search(r'(\w+), (\w+): (\S+)', contactInfo)
#分组   r按原生字符处理比如.
print(match.group(1))
print(match.group(2))
print(match.group(3))
