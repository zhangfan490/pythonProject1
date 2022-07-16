#!/usr/bin/python
# -*- coding: UTF-8 -*-
import money
#定义工资查询的模块
def select_money():
    current_money =money.save_money
    if current_money == 2000:
        print("现有存款：" + str(current_money))
    else:
        print("还未收到工资")