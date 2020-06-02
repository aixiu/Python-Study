#!/usr/bin/env python
# -*- coding: utf-8 -*-


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

