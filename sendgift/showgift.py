#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from gift import have_gift

import gift

#展示礼物的方法
def show():
    have_gift = gift.have_gift
    if have_gift == True:

        print("收到礼物了，好开心")
    else:
        print("没有礼物")