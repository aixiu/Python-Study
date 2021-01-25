#!/usr/bin/env python
# -*- coding: utf-8 -*-


name = "毛毛"
print("%s, 今天你开心嘛!" % name)  # 第一种 % 号：

print("{0}, 今天你开心嘛".format(name))  # 第一种 format 号：

print(f"{name}, 今天你开心嘛!")  # f-字符串格式化


# 注：
# 第一种 与c语言的printf()函数相似 采用%传入参数
# % 后实质上是元组，可以元组的方式传入多个参数。

# 第二种 Python2.6 新增了一种格式化字符串的函数 str.format()
# {}内数字可以省略，数字可以选择传入的参数的顺序

# 第三种 Python3.6 新增了一种f-字符串格式化 运行时使用format()协议进行格式化


# 常用：

print('\n{:=^40}'.format('华丽的分割线'))
print(f'10年后共有: {money:.2f}')