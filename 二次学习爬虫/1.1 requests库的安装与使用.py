#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu


# https://zhuanlan.zhihu.com/p/26681429
# requests 安装 pip install requests


# requests抓取网页的通用框架
import requests

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Something Wrong!'