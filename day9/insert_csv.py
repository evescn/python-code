#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 15:31
# @Author  : Evescn
# @Site    : 
# @File    : insert_csv.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
import csv
import os
import pymysql


def sql_inert(sql, y):
    conn = pymysql.connect(host="42.123.99.43.", port=5528, user="root", password="RGkQ%vxl7JDRv2NJ", database="qyxx")
    cur = conn.cursor()
    cur.execute(sql, y)
    conn.commit()
    conn.close()


def csv_reader(local_dir):
    print(os.walk(local_dir))
    for root, dirs, files in os.walk(local_dir):
        print(files)
        for file in files:
            file_long = os.path.join(root, file)
            print(file_long)
            csvReader = csv.DictReader(open(file_long, 'r', encoding='UTF-8'))
            print(csvReader)
            for row in csvReader:
                values = row.values()
                print(values)
                if 'Program name' in values:
                    program_name = row['']
                elif 'Last edit' in values:
                    last_edit = row['']
                elif 'Ratio of Retry' in values:
                    ratio_of_retry = row[''].strip()
                elif 'Total Picked' in values:
                    total_picked = row['']
                elif 'Components picked' in values:
                    components_picked = row['']
            print('[%s][%s][%s][%s][%s][%s]' % (
            file_long, program_name, last_edit, ratio_of_retry, total_picked, components_picked))
            y = ('CJJ1', program_name, last_edit, ratio_of_retry, total_picked, components_picked)
            sql = 'insert into zhuanli (pub_date,publication_number,app_date,application_number,inventor_list,assignee_list,title,kind_code,kind_code_desc,ipc_list,ipc_desc_list,PatentNumber,MainPrefix,CountryCode,ApplicationSoure) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            print(sql)
            #sql_inert(sql, y)


if __name__ == '__main__':
    local_dir = r'G:\专利数据新增\patent-info\test1'
    csv_reader(local_dir)