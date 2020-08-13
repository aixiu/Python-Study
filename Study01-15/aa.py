#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Mon Nov 14 01:01:29 2016
 
@author: toby
"""
#知识点：原函数有返回值，加上装饰器如何拿到返回值？
 
#装饰器函数
def outer(fun): 
    def wrapper(strs): 
        print ('哈哈')
        fun(strs)
        print ('hello world!')
        # return fun(strs) #返回原函数的返回值
    return wrapper
 
@outer
def func1(arg):
    print('this is func1',arg)
    return '100' #这是原函数的返回值
 
#调用函数时，传入一个字符串作为参数
aa = func1("my name is tantianran")
print (aa)
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
