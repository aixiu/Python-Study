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
