#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
本次要爬的贴吧是<< 生活大爆炸吧 >>，生活大爆炸是我一直很喜欢的一部美剧，平时有空也会去看看吧友们都在聊些什么。所以这次选取这个吧来作为实验材料。
贴吧地址 :
http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8 
"""

# 目标分析：
# 由于是第一个实验性质爬虫，我们要做的不多，我们需要做的就是：

# 从网上爬下特定页码的网页
# 对于爬下的页面内容进行简单的筛选分析
# 找到每一篇帖子的 标题、发帖人、日期、楼层、以及跳转链接
# 将结果保存到文本。

# 前期准备：
# 看到贴吧的url地址是不是觉得很乱？有那一大串认不得的字符？

# 其实这些都是中文字符，
# %E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8

# 在编码之后就是： 生活大爆炸 。

# 链接的末尾处：&ie=utf-8 表示该连接采用的是utf-8编码。
# windows的默认编码是GBK，在处理这个连接的时候，需要我们在Python里手动设置一下，才能够成功使用。

# 接着我们翻到贴吧的第二页：

# `url: http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8&pn=50`


# 注意到没有，连接的末尾处多了一个参数&pn=50,
# 这里我们很容易就能猜到，这个参数的与页码的联系：

# &pn=0 ： 首页
# &pn=50： 第二页
# &pn=100：第三页
# &pn=50*n 第n页
# 50 表示 每一页都有50篇帖子。
# 这下我们就能通过简单的url修改，达到翻页的效果了。

""" 
我们仔细的观察一下，发现每个帖子的内容都包裹在一个li标签内：

<li class=" j_thread_list clearfix">

这样我们只要快速找出所有的符合规则的标签，

在进一步分析里面的内容，最后筛选出数据就可以了。 
"""

import requests
from bs4 import BeautifulSoup
import time

def get_html(url):
    try:
        r = requests.get(url, timeout=20)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        #这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬去其他的页面时建议使用：
        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        return r.text
    # except Exception as a:
    #     return ('ERROR', a)
    except:
        return 'ERROR'

# 具体代码的实现：
def get_content(url):
    '''
    分析贴吧的网页文件，整理信息，保存在列表变量中
    '''

    # 初始化一个列表来保存所有的帖子信息：
    comments = []
    # 首先，我们把需要爬取信息的网页下载到本地
    html = get_html(url)

    # 我们来做一锅汤
    # soup = BeautifulSoup(html, 'html.parser')
    soup = BeautifulSoup(html, 'lxml')

    # 按照之前的分析，我们找到所有具有‘ j_thread_list clearfix’属性的li标签。返回一个列表类型。
    liTags = soup.find_all('li', attrs={"class": 'j_thread_list clearfix thread_item_box'})
    # 通过循环找到每个帖子里的我们需要的信息：
    for li in liTags:
        # 初始化一个字典来存储文章信息
        comment = {}
        # 这里使用一个try except 防止爬虫找不到信息从而停止运行
        try:
            # 开始筛选信息，并保存到字典中
            comment['title'] = li.find(
            'a', attrs={"class": ['j_th_tit']}).text.strip()
            comment['link'] = "http://tieba.baidu.com/" + li.find('a', attrs={"class": ['j_th_tit']})['href']
            comment['name'] = li.find(
            'span', attrs={"class": ['tb_icon_author']}).text.strip()
            comment['time'] = li.find(
            'span', attrs={"class": ['pull-right is_show_create_time']}).text.strip()
            comment['replyNum'] = li.find(
            'span', attrs={"class": ['threadlist_rep_num center_text']}).text.strip()
            comments.append(comment)
        except:
            print('出了点小问题')

    return comments

def Out2File(dict):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中。
    '''
    with open('TTBT.txt', 'a+', encoding='utf-8') as f:
        for comment in dict:
            f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))
        print('当前页面爬取完毕')

def main(base_url, deep):
    url_list = []
    #将所有需要爬去的url存入列表
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    print('所有的网页已经下载到本地！ 开始筛选信息。。。。')

    #循环写入所有的数据
    for url in url_list:
        content = get_content(url)
        Out2File(content)
    print('所有的信息都已经保存完毕！')


base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'

# 设置需要爬取的页码数量
deep = 1


if __name__ == '__main__':
    main(base_url, deep)
    
