#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

import requests

r = requests.get('http://www.baidu.com')

print(r.text)