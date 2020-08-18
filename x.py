#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = ['{}'.format(i) for i in range(2)]

print(x)


pages = int(input("页数："))

urls = ['https://www.pexels.com/?page={}'.format(str(i)) for i in range(1, pages+1)]
# print(urls)
for i in urls:
    print(i)