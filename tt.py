#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
import time

if (len(sys.argv) >= 2):
    urls = sys.argv[1].split(',')
else:
    urls = ['http://blog.ynxiu.com/']
for i in range(0, len(urls)):
    req = requests.get(urls[i])
    print(f'第{i}号网址唤醒状态:', req, time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


class Student(object):
    
    def __init__(self, name, score):
        self.Hname = name
        self.Hscore = score

    def print_score(self):
        print('%s: %s' % (self.Hname, self.Hscore))

    def get_grade(self):
        if self.Hscore >= 90:
            return 'A'
        elif self.Hscore >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('liang', 88)
print(bart.Hname, bart.Hscore, bart.get_grade())


age = 18
name = '老牛'

print(f'your name is {name},and your age is {age}')

print('your name is {},and your age is {}'.format(name, age))