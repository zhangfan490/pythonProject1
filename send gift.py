#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
发礼物
1、礼物的标识
2、发礼物的方法
3、展示礼物的方法
4、启动
'''
#拥有礼物的标识
have_gift = False

#发礼物的方法
def send():
    print("发礼物了，好开心")
    global have_gift
    have_gift = True

#展示礼物的方法
def show():
    if have_gift == True:

        print("收到礼物了，好开心")
    else:
        print("没有礼物")

#启动
if __name__ == '__main__':
    send()
    show()

