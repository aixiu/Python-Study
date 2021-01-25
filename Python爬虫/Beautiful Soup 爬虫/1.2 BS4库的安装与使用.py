#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 从网页中获取
# import requests
# from bs4 import BeautifulSoup

# r = requests.get('http://www.baidu.com')
# r.encoding = r.apparent_encoding

# soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())



# 从本地html中获取
from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup(open('./demo.html'), 'html.parser')   # python 默认解析器  html.parser
print(soup.prettify())

print('网页title为：', soup.title)
print('title的name值为：', soup.title.name)
print('title中的字符串String为：', soup.title.string)
print('文档的第一个找到的段落为：', soup.p)
print('title的父亲节点的name属性为：', soup.title.parent.name)
print('找到的p的class属性值为：', soup.p['class'])
print('找到第一个a标签为：', soup.a)
print('找到所有的a标签为：', soup.find_all('a'))
print('找到id值等于3的a标签为：', soup.find(id="link3"))

print('\n{:=^40}\n'.format('华丽的分割线'))

# 找到文档中所有 <a> 标签的链接：

for i in soup.find_all('a'):
    print(i.get('href'))

#我们可以通过get_text 方法 快速得到源文件中的所有text内容。
print(soup.get_text())

'''
将一段文档传入BeautifulSoup 的构造方法,就能得到一个文档的对象,
可以传入一段字符串或一个文件句柄。如下：

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"))
soup = BeautifulSoup("<html>data</html>")
'''

# 请仔细观察最前面的html文件


# #找到文档的title
# soup.title
# # <title>The Dormouse's story</title>

# #title的name值
# soup.title.name
# # u'title'

# #title中的字符串String
# soup.title.string
# # u'The Dormouse's story'

# #title的父亲节点的name属性
# soup.title.parent.name
# # u'head'

# #文档的第一个找到的段落
# soup.p
# # <p class="title"><b>The Dormouse's story</b></p>

# #找到的p的class属性值
# soup.p['class']
# # u'title'

# #找到a标签
# soup.a
# # http://example.com/elsie" id="link1">Elsie

# #找到所有的a标签
# soup.find_all('a')
# # [http://example.com/elsie" id="link1">Elsie,
# #  http://example.com/lacie" id="link2">Lacie,
# #  http://example.com/tillie" id="link3">Tillie]

# #找到id值等于3的a标签
# soup.find(id="link3")
# # http://example.com/tillie" id="link3">Tillie