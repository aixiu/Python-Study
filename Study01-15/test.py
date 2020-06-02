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
