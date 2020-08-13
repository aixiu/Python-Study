#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Human:
    """
    此类主要是构建人类
    """
    mind = '有思想'  # 第一部分：静态属性 属性 静态变量 静态字段
    dic = {}
    l1 = []
    def work(self): # 第二部分：方法 函数 动态属性
        # print(self)
        print('人类会工作')
# print(Human.__dict__)
# print(Human.__dict__['mind'])



# daqian = input('打钱OR滚蛋：')
# cont = 0
# while daqian == '打钱'::
#     if daqian == '打钱':
#         print('解决')
#         break
#     else:
#         print('哪来的去哪')
#         cont += 1


# daqian = input('打钱OR滚蛋：')
# cont = 0
# while True:
#     if daqian == '打钱':
#         print('解决')
#         break
#     else:
#         print('哪来的去哪')
#         cont += 1
#         if cont == 3:
#             break


def daqian(qian):
    if qian == '打钱':
        print('解决')
    else:
        print('滚蛋')

daqian('打钱')
daqian('不给')