#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-5-30 下午4:08
# @Author  : Evescn
# @Site    : 
# @File    : spider.py
# @Software: PyCharm Community Edition

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
from pyquery import PyQuery as pq
import pymongo
from config import *


# browser = webdriver.Chrome()
browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
wait = WebDriverWait(browser, 10)

browser.set_window_size(1400, 900)

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def search():
    print('开始检索')
    try:
        browser.get('https://www.taobao.com')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
        )
        input.send_keys('美食')
        submit.click()
        total = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        # print(type(total))
        get_products()
        return total.text
    except TimeoutError:
        return search()


def next_page(page_number):
    print('到%s页了' % page_number)
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
        )
        input.clear()
        input.send_keys(page_number)
        submit.click()
        # print(page_number)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
        get_products()
    except TimeoutError:
        return next_page(page_number)


def get_products():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item'))
    )
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    # print(items)
    for item in items:
        # print(item)
        product = {
            'image': item.find('.pic .img').attr('data-src')[2:],
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text(),
        }
        # print(product)
        sava_to_mongo(product)


def sava_to_mongo(result):
    try:
        if db[MONGB_TABLE].insert(result):
            print("插入mongodb成功", result)
    except Exception:
        print("出错了")


def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    # print(total)
    for i in range(1, total):
        next_page(i+1)
        # time.sleep(3)


if __name__ == '__main__':
    main()
