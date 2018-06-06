#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-6-6 上午10:34
# @Author  : Evescn
# @Site    : 
# @File    : spider.py
# @Software: PyCharm Community Edition

from urllib.parse import urlencode
import requests
from requests.exceptions import ConnectionError
import time
from pyquery import PyQuery as pq


base_url = 'http://weixin.sogou.com/weixin?'
headers = {
    'Cookie': 'SUV=00E3555BB695A0D95B07B3BBC0D74895; CXID=8B73A562F2290DE60E30F0B0E283F53C; SUID=C52F457D5B68860A5B0CB0C500096704; IPLOC=CN5101; ABTEST=6|1528103194|v1; SNUID=FEB2D8E09D99F050DD81DA089DE03B2D; weixinIndexVisited=1; sw_uuid=8911123705; dt_ssuid=2161327776; ssuid=9044929720; pex=C864C03270DED3DD8A06887A372DA219231FFAC25A9D64AE09E82AED12E416AC; ad=Flllllllll2bRaRVlllllV7qRnylllllKUUseyllllwlllllxVxlw@@@@@@@@@@@; ld=wZllllllll2bVyW8lllllV7qRBklllllKUUmYkllllwlllllxllll5@@@@@@@@@@; pgv_pvi=384444416; SMYUV=1528161099723618; JSESSIONID=aaaOTqKQWXzCJb4rm9knw; sct=4; ppinf=5|1528253149|1529462749|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTUlODclQTElRTYlOTklQUZ8Y3J0OjEwOjE1MjgyNTMxNDl8cmVmbmljazoxODolRTUlODclQTElRTYlOTklQUZ8dXNlcmlkOjQ0Om85dDJsdURrb3pnSTRKd0dweUVULVNQSXdLQ1lAd2VpeGluLnNvaHUuY29tfA; pprdig=yCdlC_CjXNGaciQUSyW-LR_GH3Gagxfb_1yE9Kegos6fNJDKPS50fClWnboLUYaz8vcnzcQ3svdl6SQqBe1DOPwQxV0HBXEh6D8FhNQCFsxB17ECz4Q6AnqPOGO6VGyrwc0iOF__ZQvhWnR92X55ReDAN4Gy6nc_wUDrtciWSXQ; sgid=04-33301577-AVsXSt33QzricvdxMaW1Ml3g; ppmdig=15282531490000009e165726b45d951b6684fd08279fad7b',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
KEYWORD = '风景'
PROXY_POOL_URL = 'http://127.0.0.1:5000/get'
PROXY = None
MAX_COUNT = 5

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def get_html(url, count=1):
    print('Crawling', url)
    print('Trying Count', count)
    global PROXY
    if count >= MAX_COUNT:
        print('Tried Too Many Counts')
        return None
    try:
        if PROXY:
            proxies = {
                'http': 'http://' + PROXY
            }
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            # Need Proxy
            print('302 ')
            time.sleep(1)
            PROXY = get_proxy()
            print('PROXY', PROXY)
            if PROXY:
                print('Using Proxy', PROXY)
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred!', e.args)
        PROXY = get_proxy()
        count += 1
        return get_html(url, count)


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    url = base_url + urlencode(data)
    html = get_html(url)
    return html

# def

def main():
    for page in range(1, 100):
        html = get_index('KEYWORD', page)
        print(html)


if __name__ == '__main__':
    main()