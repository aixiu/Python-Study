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




def eat():
    lst = []
    for i in range(1,11):
        lst.append('包子'+str(i))
    return lst
e = eat()
print(e)


# def eat():
#     for i in range(1,11):
#         yield '包子'+str(i)
# e = eat()
# print(e.__next__())


def eat():
    for i in range(1,10000):
        a = yield '包子'+str(i)
        print('a is',a)
        b = yield '窝窝头'
        print('b is', b)
e = eat()
print(e.__next__())
print(e.send('大葱'))
# print(e.send('大蒜'))


def func():
    lst1 = ['卫龙','老冰棍','北冰洋','牛羊配']
    lst2 = ['馒头','花卷','豆包','大饼']
    yield from lst1
    yield from lst2
g = func()
for i in g:
    print(i)


lst = ['python%s' % i for i in range(1, 19)]
print(lst)

lst = ['python{}'.format(i) for i in range(1, 20)]
print(lst)


import time
def f():
    start_time = time.time()
    print("hello")
    time.sleep(1)
    print("world")
    end_time = time.time()

    execution_time = (end_time - start_time)*1000
    print("time is %d ms" %execution_time)
    print(start_time)
    print(start_time)
    
f()