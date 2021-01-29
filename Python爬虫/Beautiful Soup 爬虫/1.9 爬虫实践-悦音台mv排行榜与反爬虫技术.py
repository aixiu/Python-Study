#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def get_html_text(url):
    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()
        r.encoding = ('utr-8')
        return r.text
    except:
        return 'something wrong'


def get_jokes(url):
    '''
    返回当前url页面的糗百的
    段子作者，主体，热评
    返回类型：列表
    '''
    joke_list = []

    html = get_html_text(url).strip()
    soup = BeautifulSoup(html, 'lxml')

    articles = soup.find_all('div', class_='article block untagged mb15 typs_hot')

    for article in articles:
        body = article.find('span').text.strip().replace('\n', ' ')
        author = article.find('img')['alt']
        try:
            comment = article.find('div', class_='main-text').contents[0].strip()
        except:
            comment = '暂时没有热评'
            
        try:
            hotauthor = article.find('span', class_='cmt-name').text.strip()
        except:
            hotauthor = '暂无'

        try:
            stats_vote = article.select('span > i')[0].string.strip()
        except:
            stats_vote = '暂无'

        try:
            stats_comments = article.select('a > i')[0].string.strip()
        except:
            stats_comments = '暂无'

        joke = '作者：{}\n{}\n热评 >>> {}{}\n好笑指数：{} · 评论数：{}\n'.format(author, body, hotauthor, comment, stats_vote, stats_comments)
        joke_list.append(joke)
        # joke_list.append(author)
        for i in joke_list:
            print(i)
            # print('\n{:=^40}\n'.format('华丽的分割线'))

    # return joke_list
    return '完成'


# test:

url = 'https://www.qiushibaike.com/text/page/1/'

a = get_jokes(url)
print(a)
