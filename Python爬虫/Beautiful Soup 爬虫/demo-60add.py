#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
本次要爬的是<< http://60addons.com/ >>，插件名和所有插件下载页面。
贴吧地址 :
http://60addons.com/bbs/new/index/1
"""

from bs4 import BeautifulSoup
import requests

def get_html(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        return r.text
    except:
        return 'ERROR'
        

def get_content(url):
    comments = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    liTags = soup.find_all('div', attrs={'class': 'col-sm-10 list-info'})
    # return liTags
    for li in liTags:
        comment = {}
        try:
            comment['title'] = li.find('a', attrs={'class': 'list-post-link'}).string.strip()  # 获取a下的所有文本（嵌套标签的文本）
            # comment['fenname'] = li.find(['span', 'a'], attrs={'class': 'list-author'}).text.strip()
            comment['link'] = "http://60addons.com" + li.find('a', attrs={'class': 'list-post-link'})['href']
            # comment['count'] = li.find('span', attrs={'class': 'list-comments'}).string.strip()

            # 处理相同span下边的第二个数据
            hot = li.find_all('span', attrs={'class': 'list-comments'})
            for i in hot:
                comment['count'] = hot[1].string[3:]

            comments.append(comment)

        except:
            print('出了点小问题')
        # print(li)
    
    return comments

def Out2File(dict):
    with open('60addlist.txt', 'a+', encoding='utf-8') as f:
        for comment in dict:
            # f.write(f'标题： {comment['title']} \t 链接： {comment['link']} \t 下载次数： {comment['count']}') 
            f.write('插件名： {} \t 链接： {} \t 浏览次数： {} \n'.format(comment['title'], comment['link'], comment['count'])) 
        # print('当前页面爬取完毕，链接地址：{}')

def main(base_url, deep):
    url_list = []
    for i in range(1, deep+1):
        url_list.append('{}{}'.format(base_url, str(i)))
    print('所有的网页已经准备就绪！ 开始筛选信息。。。。')
    
    #循环写入所有的数据
    for url in url_list:
        content = get_content(url)
        print('当前地址：{}'.format(url))
        Out2File(content)
        print('当前页面爬取完毕!')
    print('所有的信息都已经保存完毕！')
    # print(url_list)

# 设置需要爬取的页码数量
deep = 2
base_url = 'http://60addons.com/bbs/new/index/'


if __name__ == '__main__':
    main(base_url, deep)

# print(get_content('http://60addons.com/bbs/new/index/'))


