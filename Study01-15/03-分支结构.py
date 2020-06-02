#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
猜数字，10以内的正整数，并记录猜了多少次
'''

count = 0

print('{:*^40}'.format('重要提示：猜数字，输入10以内的正整数'))
while True:
    am = input('{}'.format('请输入一个数>>>'))
    if am == '6':
        print('{:=^40}'.format('猜对啦！'))
        break
    elif am > '6':
        print('{:=^40}'.format('你输入的数大了点，请重新输入。'))
        count += 1
    else:
        print('{:=^40}'.format('你输入的数小了点，请重新输入。'))
        count += 1

if count <= 2:
    print('你一共猜了>>> {}次，真聪明！'.format(count))
else:
    print('你一共猜了>>> {}次，够笨的'.format(count))    
