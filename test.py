#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

session = requests.session()

url = 'http://www.baiu.com'

res = session.get(url)

print(res)
