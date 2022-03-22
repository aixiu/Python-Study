#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    模拟header的user-agent字段，
    返回一个随机的user-agent字典类型的键值对

    使用代理池。
    '''

import requests
import random
from bs4 import BeautifulSoup


def get_html(url):
    try:
        r = requests.get(url,  timeout=30, headers=get_agent(), proxies=get_proxy())
        r.raise_for_status
        # 我手动测试了编码。并设置好，这样有助于效率的提升
        r.encoding = ('utr-8')
        return r.text
    except:
        return "Someting Wrong！"


def get_agent():
    '''
    模拟header的user-agent字段，
    返回一个随机的user-agent字典类型的键值对
    '''
    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
    fakeheader = {}
    fakeheader['User-agent'] = agents[random.randint(0, len(agents))]
    return fakeheader


def get_proxy():
    '''
    简答模拟代理池
    返回一个字典类型的键值对，
    '''
    proxy = ["http://116.211.143.11:80",
             "http://183.1.86.235:8118",
             "http://183.32.88.244:808",
             "http://121.40.42.35:9999",
             "http://222.94.148.210:808"]
    fakepxs = {}
    fakepxs['http'] = proxy[random.randint(0, len(proxy))]
    return fakepxs

def get_content(url):
    '''
    爬取每一类型小说排行榜，
    按顺序写入文件，
    文件内容为 小说名字+小说链接
    将内容保存到列表
    并且返回一个装满url链接的列表
    '''
    url_list = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    movies_info = soup.find_all('div', class_='info')
    
    # for i in movies_info:
    #     # try:
    #     #     diqu = article.find('span', class_='pl')
    #     #     print(diqu)
    #     # except:
    #     #     diqu = '暂无'
    #     print(i)
        

    
    
    
    return movies_info


print(get_content('https://movie.douban.com/subject/27605698/?from=subject-page'))
