#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bs4

#首先我们先将 html 文件以 lxml 的方式做成一锅汤
# soup = bs4.BeautifulSoup(open('./demo.html'), 'html.parser')
soup = bs4.BeautifulSoup(open('./demo.html'), 'lxml')
# soup = bs4.BeautifulSoup(open('./demo.html'), 'lxml', from_encoding='utf-8')

# print(soup.prettify())

# bs4 库首先将传入的字符串或文件句柄转换为 Unicode的类型，
# 这样，我们在抓取中文信息的时候，就不会有很麻烦的编码问题了。
# 当然，有一些生僻的编码 如：‘big5’，就需要我们手动设置编码：

# soup = BeautifulSoup(markup, from_encoding="编码方式")


# 搜索文档树的最简单的方法就是搜索你想获取tag的的name：
# soup.head
# # <head><title>The Dormouse's story</title></head>

# soup.title
# # <title>The Dormouse's story</title>

# 如果你还想更深入的获得更小的tag：例如我们想找到body下的被b标签包裹的部分

# soup.body.b
# # <b>The Dormouse's story</b>
# 但是这个方法只能找到按顺序第一个出现的tag

print(soup.head)
print(soup.title)
print(soup.body.b)

# 获取所有的标签呢？
# 这个时候需要find_all()方法，他返回一个列表类型

tag = soup.find_all('a')
print(tag)

#假设我们要找到a标签中的第二个元素：
need = tag[1]
print(need)

print('\n{:=^40}'.format('华丽的分割线'))
# tag的.contents属性可以将tag的子节点以列表的方式输出：
# 如：

head_tag = soup.head
print(head_tag)
print(head_tag.contents)

print('\n{:=^40}'.format('华丽的分割线'))

title_tag =  head_tag.contents[0]
print(title_tag)
print(title_tag.contents)

print('\n{:=^40}'.format('华丽的分割线'))

# 另外通过tag的 .children生成器，可以对tag的子节点进行循环：
for i  in title_tag.children:
    print(i)


# 本文链接：https://zhuanlan.zhihu.com/p/26691931