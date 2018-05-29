#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-5-29 下午2:58
# @Author  : Evescn
# @Site    : 
# @File    : spider.py
# @Software: PyCharm Community Edition
import json
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException
import re


def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def get_result(html):
    pattern = re.compile('<dd>.*?board-inde.*?>(.*?)</i>.*?data-src="(.*?)".*?title="(.*?)".*?'
                         +'star">(.*?)</p>.*?easetime">(.*?)</p>.*?integer">(.*?)</i>.*?ction'+
                         '">(.*?)</i>.*?</dd>', re.S)

    # pattern = re.compile('<dd>.*?board-index.*?">(\d+)</i>.*?data-src="(.*?)".*?s'
    #                      +'tar">(.*?)</p>.*?time">(.*?)</p.*?integer">(.*?)</i>.*?t'
    #                      +'ion">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'scode': item[5]+item[6],
        }


def write_file(content):
    with open ('result.txt', 'a') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_url(url)
    # print(html)
    # data = get_result(html)
    for item in get_result(html):
        write_file(item)


if __name__ == '__main__':
    # for i in range(10):
    #     main(i*10)
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])
