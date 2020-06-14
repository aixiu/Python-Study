#!/usr/bin/env python
# -*- coding: utf-8 -*-

lst = [1,3,2,5,4]


def sq(x):
    return x*x

print(map(sq, lst))
print(type(map(sq, lst)))
print(list(map(sq, lst)))


def func():   
    print("吃了么")
def func2(fn):   
    print("我是func2")   
    fn()    # 执行传递过来的fn   
    print("我是func2")
func2(func)     # 把函数func当成参数传递给func2的参数fn.



def func_1():   
    print("这里是函数1")   
    def func_2():       
        print("这里是函数2")   
    print("这里是函数1")   
    return func_2
fn = func_1()  
# 执行函数1.  函数1返回的是函数2, 这时fn指向的就是上面函数2
fn()    # 执行func_2函数




def func1():  
    def func2(): 
        s = '嘿嘿'
        def func3():       
            print(s)      
        return func3 
    return func2

aa = func1()

print(aa()())


lst = []
for i in range(10, 41):
    if i % 2 == 0:
        lst.append(i)

print(lst[3])
print(lst[4:7])

llst = lst[4:7]

print(max(llst))
print(min(llst))
print(sum(llst))
print(len(llst))

llst.remove(max(llst))
print(llst)

llst.remove(min(llst))
print(llst)



