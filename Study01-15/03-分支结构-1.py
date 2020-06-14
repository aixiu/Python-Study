#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
使用循环输出1~100所有整数。
'''
LL = []
for i in range(1, 101):
    LL.append(i)

print(LL)


'''
使用循环输出 1 2 3 4 5 6 8 9 10，即：10以内除7以外的整数。
'''

for i in range(1, 11):
    if i == 7:
        pass
    else:
        print(i)

print('{:*^20}'.format('华丽的分割线'))

for i in range(1, 11):
    if i != 7:
        print(i)

print('{:*^20}'.format('华丽的分割线'))

for i in range(1, 11):
    if i == 7:
        continue
    else:
        print(i)

print('{:*^20}'.format('华丽的分割线'))

count = 1
while count < 11:
    if count == 7:
        pass
    else:
        print(count)
    count += 1


'''
输出 1~100 内的所有奇数。
'''

ll = []

for i in range(1, 101):
    if i % 2 != 0:
        ll.append(i)
print(ll)

lls= []
for i in range(1, 101, 2):
    lls.append(i)

print(lls)


'''
输出 1~100 内的所有偶数。
'''
lls= []
for i in range(2, 101, 2):
    lls.append(i)

print(lls)


ll = []

for i in range(1, 101):
    if i % 2 == 0:
        ll.append(i)
print(ll)


ll = []

y = 0

while y < 100:
    y += 1
    if y % 2 != 0:
        continue
    ll.append(y)

print(ll)
    

'''
求 1~100 的所有整数的和。
'''
AA = 0
for i in range(1, 101):
    AA += i
print(AA)



ll = []

for i in range(1, 101):
    ll.append(i)

print(sum(ll))


'''
输出10~1 所有整数。
'''

for i in range(10, 0, -1):
    print(i)

ll = []
for i in range(1, 11):
    ll.append(i)
ll.reverse()
print(ll)