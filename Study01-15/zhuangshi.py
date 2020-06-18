#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

def use_logging(func):
    
    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

def foo():
    print('i am foo')

foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
foo()                   # 执行foo()就相当于执行 wrapper()



def decorator(func):
    def wrapper(*args,**kargs):
        print('I love Python!')
        func()
    return wrapper
 
@decorator
def fun():
    print('test')


fun()


def record_request(data_param):
    def func_outer(func):
        def func_inner(*args, **kwargs):
            print("获取到的函数参数：",args)
            print("---------函数运行之前-----")
            func(*args, **kwargs)
            print('{}'.format(data_param))
            print('{}'.format(data_param))
            print("---------函数运行之后-----")
        return func_inner
    return func_outer
 
data={"name":"张三","age":23}
@record_request("baidu_spider")
def test(res):
    print("函数测试执行内容。。。。")
 
test(data)