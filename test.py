#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

session = requests.session()

# url = 'https://www.douban.com/search?q=python&cat=1001'

# res = session.get(url)

# print(res)

# r = requests.get(url, params={'q': 'python', 'cat': '1001'})
# print(r.url)

r = requests.get('https://www.douban.com/search?q=python&cat=1001&format=json')
print(r.json)


