#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-6-14 下午2:59
# @Author  : Evescn
# @Site    : 
# @File    : request-lx.py
# @Software: PyCharm Community Edition

# 实例引入
# import requests
#
# response = requests.get("https://www.baidu.com")
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)

# 各种请求方式
# import requests

# requests.post("http://httpbin.org/post")
# requests.put("http://httpbin.org/put")
# requests.delete("http://httpbin.org/delete")
# requests.head("http://httpbin.org/head")
# requests.options("http://httpbin.org/options")
# response = requests.get("http://httpbin.org/get")
# print(type(response))
# print(response.status_code)
# print(response.text)

# 请求
# 基本GET请求
# import requests
#
# response = requests.get("http://httpbin.org/get")
# print(response.text)

# 带参数GET请求
# import requests
#
# response = requests.get("http://httpbin.org/get?name=evescn&age=22")
# print(response.text)
#
#
# import requests
# data = {
#     'name': 'gmkk',
#     'age': 22
# }
#
# response = requests.get("http://httpbin.org/get", params=data)
# print(response.text)


# 解析json
# import requests
#
# response = requests.get("http://httpbin.org/get")
# print(type(response.text))
# print(response.json())
# print(type(response.json()))


# 获取二进制数据
# import requests
#
# response = requests.get("http://httpbin.org/get")
# print(type(response.text),type(response.content))
# print(response.text)
# print(response.content)

# import requests
#
# response = requests.get("https://github.com/favicon.ico")
# print(response.content)
# with open('favicon.ico', 'wb') as f:
#     f.write(response.content)
#     f.close()


# 添加headers
# import requests
#
# response = requests.get("https://www.zhihu.com/explore")
# print(response.text)

# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
# }
# response = requests.get("https://www.zhihu.com/explore", headers=headers)
# print(response.text)

# 基本POST请求
# import requests
#
# data = {
#     'name': 'evescn',
#     'age': 22
# }
# response = requests.post("http://httpbin.org/post", data=data)
# print(response.text)

# import requests
#
# data = {
#     'name': 'evescn',
#     'age': 22
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
# }
# response = requests.post("http://httpbin.org/post", data=data, headers=headers)
# print(response.json())

# 相应
# reponse属性
# import requests
#
# response = requests.get('http://www.jianshu.com')
# print(type(response.status_code),response.status_code)
# print(type(response.headers),response.headers)
# print(type(response.cookies),response.cookies)
# print(type(response.url),response.url)
# print(type(response.history),response.history)


# 状态码判断
# import requests
#
# response = requests.get('http://www.jianshu.com')
# exit() if not response.status_code == requests.codes.forbidden else print('Request Successfully')
#
# import requests
#
# response = requests.get('http://www.jianshu.com')
# exit() if not response.status_code == 403 else print('Request Successfully')

# 高级操作
# 文件上传
# import requests
#
# files = {
#     'file': open('favicon.ico', 'rb')
# }
# response = requests.post("http://httpbin.org/post", files=files)
# print(response.text)

# 获取cookie







import requests

headers = {
    'Cookie': 'SUV=00E3555BB695A0D95B07B3BBC0D74895; CXID=8B73A562F2290DE60E30F0B0E283F53C; SUID=C52F457D5B68860A5B0CB0C500096704; IPLOC=CN5101; ABTEST=6|1528103194|v1; SNUID=FEB2D8E09D99F050DD81DA089DE03B2D; weixinIndexVisited=1; sw_uuid=8911123705; dt_ssuid=2161327776; ssuid=9044929720; pex=C864C03270DED3DD8A06887A372DA219231FFAC25A9D64AE09E82AED12E416AC; ad=Flllllllll2bRaRVlllllV7qRnylllllKUUseyllllwlllllxVxlw@@@@@@@@@@@; ld=wZllllllll2bVyW8lllllV7qRBklllllKUUmYkllllwlllllxllll5@@@@@@@@@@; pgv_pvi=384444416; SMYUV=1528161099723618; JSESSIONID=aaaOTqKQWXzCJb4rm9knw; sct=4; ppinf=5|1528253149|1529462749|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTUlODclQTElRTYlOTklQUZ8Y3J0OjEwOjE1MjgyNTMxNDl8cmVmbmljazoxODolRTUlODclQTElRTYlOTklQUZ8dXNlcmlkOjQ0Om85dDJsdURrb3pnSTRKd0dweUVULVNQSXdLQ1lAd2VpeGluLnNvaHUuY29tfA; pprdig=yCdlC_CjXNGaciQUSyW-LR_GH3Gagxfb_1yE9Kegos6fNJDKPS50fClWnboLUYaz8vcnzcQ3svdl6SQqBe1DOPwQxV0HBXEh6D8FhNQCFsxB17ECz4Q6AnqPOGO6VGyrwc0iOF__ZQvhWnR92X55ReDAN4Gy6nc_wUDrtciWSXQ; sgid=04-33301577-AVsXSt33QzricvdxMaW1Ml3g; ppmdig=15282531490000009e165726b45d951b6684fd08279fad7b',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

# proxies = {
#     'http': 'socks5://127.0.0.1:1080',
#     'https': 'socks5://127.0.0.1:1080'
# }

proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'https://127.0.0.1:1080'
}

response = requests.get('http://httpbin.org/get', proxies=proxies)
print(response.status_code)
print(response.text)

# response = requests.get('https://www.google.com', headers=headers, proxies=proxies)
# print(response.status_code)
# print(response.text)