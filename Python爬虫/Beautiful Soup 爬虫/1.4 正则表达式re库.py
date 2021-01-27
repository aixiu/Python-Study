#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 正则表达式是用来简洁表达一组字符串的表达式,
# 或者你可以将它理解为高级版的 通配符 表达式

'''
元字符 （参见 python 模块 re 文档）

.                    匹配任意字符（不包括换行符）
^                    匹配开始位置，多行模式下匹配每一行的开始
$                    匹配结束位置，多行模式下匹配每一行的结束
*                    匹配前一个元字符0到多次
+                    匹配前一个元字符1到多次
?                    匹配前一个元字符0到1次
{m,n}                匹配前一个元字符m到n次
\\                   转义字符，跟在其后的字符将失去作为特殊元字符的含义，例如\\.只能匹配.，不能再匹配任意字符
[]                   字符集，一个字符的集合，可匹配其中任意一个字符
|                    逻辑表达式 或 ，比如 a|b 代表可匹配 a 或者 b
(...)                分组，默认为捕获，即被分组的内容可以被单独取出，默认每个分组有个索引，从 1 开始，按照"("的顺序决定索引值
(?iLmsux)            分组中可以设置模式，iLmsux之中的每个字符代表一个模式,用法参见 模式 I
(?:...)              分组的不捕获模式，计算索引时会跳过这个分组
(?P<name>...)        分组的命名模式，取此分组中的内容时可以使用索引也可以使用name
(?P=name)            分组的引用模式，可在同一个正则表达式用引用前面命名过的正则
(?#...)              注释，不影响正则表达式其它部分,用法参见 模式 I
(?=...)              顺序肯定环视，表示所在位置右侧能够匹配括号内正则
(?!...)              顺序否定环视，表示所在位置右侧不能匹配括号内正则
(?<=...)             逆序肯定环视，表示所在位置左侧能够匹配括号内正则
(?<!...)             逆序否定环视，表示所在位置左侧不能匹配括号内正则
(?(id/name)yes|no)   若前面指定id或name的分区匹配成功则执行yes处的正则，否则执行no处的正则
\number              匹配和前面索引为number的分组捕获到的内容一样的字符串
\A                   匹配字符串开始位置，忽略多行模式
\Z                   匹配字符串结束位置，忽略多行模式
\b                   匹配位于单词开始或结束位置的空字符串
\B                   匹配不位于单词开始或结束位置的空字符串
\d                   匹配一个数字， 相当于 [0-9]
\D                   匹配非数字,相当于 [^0-9]
\s                   匹配任意空白字符， 相当于 [ \t\n\r\f\v]
\S                   匹配非空白字符，相当于 [^ \t\n\r\f\v]
\w                   匹配数字、字母、下划线中任意一个字符， 相当于 [a-zA-Z0-9_]
\W                   匹配非数字、字母、下划线中的任意字符，相当于 [^a-zA-Z0-9_]
'''

# 举个例子：
import re

test = 'python is the best language , pretty good !'

p = re.findall('p+', test)

print(p)  # ['p', 'p']


# 我们着重讲一下 re.search这个函数：
'''
re.search(pattern, string, flags=0) 
在一个字符串中搜索匹配正则表达式的第一个位置返回match对象
∙ pattern : 正则表达式的字符串或原生字符串表示 
∙ string : 待匹配字符串
∙ flags : 正则表达式使用时的控制标记
'''

str1 = 'hello , world ,life is short ,use Python .WHAT? '

a = re.search(r'\w+',str1)
print(a.group())    #  hello


# 我们再来说另一个常用函数re.findall()
'''
re.findall(pattern, string, flags=0) 
搜索字符串，以列表类型返回全部能匹配的子串
∙ pattern : 正则表达式的字符串或原生字符串表示 
∙ string : 待匹配字符串
∙ flags : 正则表达式使用时的控制标记
'''

c = re.findall(r'\w+',str1)
print (c)
#['hello', 'world', 'life', 'is', 'short', 'use', 'Python', 'WHAT']

print('\n{:=^40}'.format('华丽的分割线'))

str1 = 'hello , world ,life is short ,use Python .WHAT? '
str2 = 'hssso'

# re.compile 该函数根据包含的正则表达式的字符串创建模式对象
re1 = re.compile(r'h.{3}o')
print(re1.findall(str1))
print(re1.findall(str2))


# 本文链接：https://zhuanlan.zhihu.com/p/26701898