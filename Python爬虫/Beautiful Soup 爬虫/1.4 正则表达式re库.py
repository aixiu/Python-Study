#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 正则表达式是用来简洁表达一组字符串的表达式,
# 或者你可以将它理解为高级版的 通配符 表达式

# 举个例子：
import re

test = 'python is the best language , pretty good !'

p = re.findall('p+', test)

print(p)