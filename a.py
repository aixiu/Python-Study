#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu



name = 'alex'   #正确的用户名
passwd = '123456'  #正确的密码
lock_usr = []   #锁定账号列表
 
for i in range(0, 3):
    usr_name = input("用户名：")
    usr_passwd = input("密码：")
    if usr_name == name and usr_passwd == passwd:
        print("玩命加载中...")
        break
    elif name != usr_name or passwd != usr_passwd:
        if i < 2:
            print("用户名密码错误，请重新输入！")
        else:
            lock_usr.append(usr_name)     #将输入错误三次的的账号添加到锁定列表中
            print("对不起！机会只有三次，您的账号密码被锁定")
    elif usr_name in lock_usr:
        print("该账号已锁定，请解锁后登陆")
        
print(lock_usr)