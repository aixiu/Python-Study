#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# https://zhuanlan.zhihu.com/p/26683864
# bs4库的安装  pip install beautifulsoup4


# https://zhuanlan.zhihu.com/p/26691931
# lxml解析器的安装：
# pip install lxml


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 手动设置编码： soup = BeautifulSoup(markup, from_encoding="编码方式")
import bs4

#首先我们先将html文件已lxml的方式做成一锅汤
soup = bs4.BeautifulSoup(html_doc, 'lxml')
# print(soup.prettify())

# 搜索文档树的最简单的方法就是搜索你想获取tag的的name：
print(soup.head)
print(soup.title)
# 如果你还想更深入的获得更小的tag：例如我们想找到body下的被b标签包裹的部分
print(soup.body.b)
print(soup.b)

# 以上方法，只能找到按顺序第一个出现的tag

# 获取所有的标签呢？
# 这个时候需要find_all()方法，他返回一个列表类型

tag = soup.find_all('a')

#假设我们要找到a标签中的第二个元素：
need = tag[1]
print(need)

# 也可以用循环打印所有的 a 标签
# for i in tag:
#     print(i)

# tag的.contents属性可以将tag的子节点以列表的方式输出：

head_tag = soup.head
print(head_tag)


