# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:19:29 2020

@author: hemo
"""


import urllib.parse
import requests
import re
import os
from os.path import join
import pandas as pd
import os
l = []

def get_url_one_page(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    html = html.text
    url_pic_this_page = re.findall(r'"objURL":"(.*?)",', html)
    url_next_page_prefix = re.findall(r'<a href="(.*?)" class="n">下一页', html)
    if len(url_next_page_prefix) != 0:
        url_next_page = 'http://image.baidu.com' + url_next_page_prefix[0]
    else:
        print("已到达最后一页！")
        url_next_page = None
    return url_pic_this_page, url_next_page


def download_pics(url_pics, count_total, key):
    count_success = 0
    for url_pic in url_pics:
        print(url_pic)
        try:
            pic = requests.get(url_pic, timeout=10)
#            ext = url_pic.split('.')[-1]
#            pic_name = join(SAVE_DIR, key + '.' + ext)
#            with open(pic_name, 'wb') as f:
#                f.write(pic.content)
            print('已找到图片: {}张'.format(count_success + 1))
            count_success += 1
        except:
            print('第{}张图片寻找失败！已跳过...'.format(count_success + 1))
            continue
        if count_success + 1 > count_total:
            print('所有{}张图片寻找完毕!'.format(count_success))
            return url_pic


def fetch_pictures(key, num_pics):
    print('[+]开始爬虫: 关键词：{}, 爬取图片数量：{} '.format(key, num_pics))
    # 1。基础网址
    url_init_base = r'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1497491098685_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1497491098685%5E00_1519X735&word='
    # 2.加上关键字的网址
    url_init = url_init_base + urllib.parse.quote(key)
    # 3。图片网址列表
    url_pic_list = []
    while True:
        url_pic_this_page, url_next_page = get_url_one_page(url=url_init)
        url_pic_list += url_pic_this_page
        if url_next_page is not None:
            url_init = url_next_page
        else:
            print('[+]图片页数已达最后！')
            break
        if len(url_pic_list) > num_pics - 1:
            print('[+]爬虫结束！')
            break
    print('[+]开始寻找图片, 请稍等...')
    return download_pics(url_pic_list, num_pics, key)

def pic(name):
    key = "电影海报 " + str(name)
    return fetch_pictures(key, 1)  # 获取图片函数

if __name__ == "__main__":
#    num_pics = 10  # 需要爬取的数量
#    SAVE_DIR = 'pic'  # 以KEY的名字新建一个文件夹
#    if not os.path.exists(SAVE_DIR):
#        os.makedirs(SAVE_DIR)
    
    file_path = 'movies1.csv' #原数据源路径
    df = pd.read_csv(file_path)

    df['COVER']=df['COVER'].astype('str')  #将空值nan由float类型转换为str类型
    
    for index, row in df.iterrows():  #遍历表格
        if row['COVER'] == 'nan':  #遇到COVER为nan的行，补充海报url
            df.at[index, 'COVER'] = pic(row['NAME'])  #dataframe修改数据
            
    df_=df[(df['COVER'].isna())].head(100)  #查找df中是否有补充url失败的行数据
    print('还有{}条数据未找到海报url'.format(len(df_)))
    
    df.to_csv(file_path.strip('.csv') + '_new.csv')  #保存补充url后的表格