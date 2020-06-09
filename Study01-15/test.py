#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import requests
import time

# print ('参数个数为:{}个参数。'.format(len(sys.argv))), len(sys.argv)
# print ('参数列表:{}'.format(str(sys.argv)))

if (len(sys.argv) >= 2):
    urls = sys.argv[1].split(',')
    print(urls)
else:
    urls = ['https://baidu.com']

for i in range(0, len(urls)):
    req = requests.get(urls[i])
    print(f'第{i}号网址唤醒状态:', req, time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]

print(len(li))

aa = li[0::2]
print(aa)

li.append('seven')
print(li)

li.insert(1, 'Tony')
print(li)

li[2] = 'Kelly'
print(li)

l2=[1,'a',3,4,'heart'] 
li.extend(l2)
print(li)

s = 'qwert'
l3 = list(s)
li.extend(l3)
print(li)

li.remove('ritian')
print(li)

li.pop(2)
print(li)

del li[2:5]
print(li)

v1 = range(1,6)

