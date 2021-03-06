#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

# 网页抓取头：
def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        # 我手动测试了编码。并设置好，这样有助于效率的提升
        r.encoding = ('utr-8')
        return r.text
    except:
        return "Someting Wrong！"

# 获取排行榜小说及其链接：
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

    # 由于小说排版的原因，历史类和完本类小说不在一个div里
    # 历史普通类小说
    category_list = soup.find_all('div', class_='layout layout-col1')
    # 完本类小说
    history_finished_list = soup.find_all('div', class_='layout layout-col1 mr0')
    
    for cate in category_list:
        name = cate.find('div', class_='layout-tit').strong.string
        with open('novel_list.csv', 'a+', encoding='utf-8') as f:
            f.write("\n小说种类：{} \n".format(name))

        # 我们直接通过style属性来定位总排行榜
        general_list = cate.find('ul', class_="txt-list txt-list-row3")
        # 找到全部的小说名字，发现他们全部都包含在li标签之中
        book_list = general_list.find_all('li')

        # 循环遍历出每一个小说的的名字，以及链接
        for book in book_list:
            link = 'http://www.qu.la' + book.a['href']
            title = book.a.string.strip()
            # title = book.a.text.strip()
            # 我们将所有文章的url地址保存在一个列表变量里
            url_list.append(link)

            # 这里使用a模式，防止清空文件
            with open('novel_list.csv', 'a', encoding='utf-8') as f:
                f.write('小说名：{:<} \t 小说地址：{:<} \n'.format(title, link))
    print('排行榜小说地址收集完毕')
                
    for cate in history_finished_list:
        name = cate.find('div', class_='layout-tit').strong.string
        with open('novel_list.csv', 'a+', encoding='utf-8') as f:
            f.write("\n小说种类：{} \n".format(name))

        # 我们直接通过style属性来定位总排行榜
        general_list = cate.find('ul', class_="txt-list txt-list-row3")
        book_list = general_list.find_all('li')

        for book in book_list:
            link = 'http://www.qu.la' + book.a['href']
            title = book.a.string.strip()
            # title = book.a.text.strip()
            url_list.append(link)

            with open('novel_list.csv', 'a', encoding='utf-8') as f:
                f.write('小说名：{:<} \t 小说地址：{:<} \n'.format(title, link))
            # print(link)
    print('完本小说地址收集完毕')
    return url_list

# 获取单本小说的所有章节链接:
def get_txt_url(url):
    '''
    获取该小说每个章节的url地址：
    并创建小说文件

    '''
    url_list = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    # 因，最新章节和第一章标签一样，且最新在上边，故，用下 [1] 来获取第一章的
    lista = soup.find_all('ul', class_='section-list fix')[1]

    for i in lista.find('a'):
        link = 'http://www.qu.la' + i.get('href')
        url_list.append(link)

    # CSS 选择器的使用 相同 DIV 下的第二个 h1
    txt_name = soup.select('div > h1')[1].string.strip()  
    with open('./小说/{}.txt'.format(txt_name), 'a+', encoding='utf-8') as f:
        f.write('小说标题：{} \n'.format(txt_name))

    return url_list, txt_name

# 获取单本小说的所有章节链接:
def get_one_txt(url, txt_name):
    '''
    获取小说每个章节的文本
    并写入到本地
    '''

    # replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，
    # 如果指定第三个参数max，则替换不超过 max 次。
    html = get_html(url).replace('<br>', ' ')
    soup = BeautifulSoup(html, 'lxml')

    try:
        txt = soup.find('div', class_='content').text.replace('chaptererror();', '')
        title = soup.find('h1', class_='title').string.strip()

        with open('./小说/{}.txt'.format(txt_name), 'a', encoding='utf-8') as f:
            f.write(title + '\n\n')
            f.write(txt)

            print('当前小说：{} 当前章节{} 已经下载完毕'.format(txt_name, title))



        # print('\n{:=^40}\n'.format('华丽的分割线'))

        # print(txt, title)
    except:
        print('someting wrong')

# def get_all_txt(url_list):
#     for url in url_list:
#         # 便利获取当前小说的所有章节的目录，
#         # 并且生成小说头文件

#         page_list, txt_name = get_txt_url(url)
        
#         """ for page_url in page_list:
#             # 遍历每一篇小说，并下载到目录
#             get_one_txt(page_url, txt_name)
#             print('当前进度 {}% '.format(url_list.index(url) / len(url_list) * 100)) """
        

    
# def main():
#     base_url = 'https://www.qu.la/paihangbang/'
#     url_list = get_content(base_url)
#     url_list = list(set(url_list))
#     txt_name = get_txt_url(url_list)
#     get_one_txt(url_list)



# if __name__ == '__main__':
#     main()
    
    
    

# name = 
# aa = get_one_txt('https://www.qu.la/book/168/2021571.html', 'aaaa')
aa = get_txt_url('https://www.qu.la/book/168/index_1.html')
# aa = get_content('https://www.qu.la/paihangbang/')
print(aa)


# 本文链接：https://zhuanlan.zhihu.com/p/26756909