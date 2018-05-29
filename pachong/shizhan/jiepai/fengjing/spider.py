#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 21:42
# @Author  : Evescn
# @Site    : 
# @File    : spider.py.py
# @Software: PyCharm
import json

import os
import pymongo
import re
import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from config import *
from hashlib import md5
from multiprocessing import Pool

client = pymongo.MongoClient('MONGO_URL')
db = client['MONGO_DB']

def get_page_index(offset):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': KEYWORD,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1,
        'from': 'gallery'
    }

    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页错误......')
        return None


def parse_page_index(html):
    data = json.loads(html)
    # print(type(data))
    # print(data)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页错误......')
        return None


def parse_page_detail(html, url):
    # print(html)
    # soup = BeautifulSoup(html, 'lxml')
    # title = soup.select('title')[0].get_text()
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    pattern = re.compile('gallery: JSON.parse\((.*?)\),', re.S)
    result = re.search(pattern, html)
    if result:
        data = json.loads(result.group(1))
        data = json.loads(data)
        print(type(data))
        if data and 'sub_images' in data.keys():
            # for image in data.get('sub_images'):
            #     yield {
            #         'title': title,
            #         'url': url,
            #         'image': image
            #     }
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for images in images: download_image(images)
            return {
                'title': title,
                'url': url,
                'images': images
            }


def save_to_mongodb(result):
    if db['MONGO_TABLE'].insert(result):
        print('存储到MongoDB成功', result)
        return True
    return False


def download_image(url):
    print('正在下载：', url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except RequestException:
        print("请求图片出错")
        return None


def save_image(content):
    file_path = '{0}/tp/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()

def main(offset):
    html = get_page_index(offset)
    # print(html)
    for url in parse_page_index(html):
        print(url)
        if url:
            html = get_page_detail(url)
        # print(html)
            if html:
                image = parse_page_detail(html, url)
                # print(image)



if __name__ == '__main__':
    # main()
    # groups = [i*20 for i in range(GROUP_START, GROUP_END)]
    # pool = Pool()
    # pool.map(main, groups)

    groups = [x * 20 for x in range(GROUP_START, GROUP_END+1)]
    pool = Pool()
    pool.map(main, groups)














