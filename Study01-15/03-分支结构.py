#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("开始运行系统")

while True:
    user = input("请输入用户名：")
    pwd =  input("请输入密码：")
    if user == 'wupeiqi' and pwd == "oldboy":
        print("登录成功")
        break
    else:
        print("用户名或密码错误，请重新登录")
print("系统结束")