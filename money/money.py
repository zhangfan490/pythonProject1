#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
'''

#原有存款
save_money = 1000

#定义发工资的模块
def send_money():
    send_money = 1000
    global save_money
    print(f"发工资前，有存款{save_money}元")
    save_money = save_money + send_money


#定义工资查询的模块
def select_money():
    if save_money == 2000:
        print(f"发了工资后，存款一共有{save_money}元")
    else:
        print(f"没有发工资，存款还是{1000}元")

#启动
if __name__ == '__main__':
    select_money()
    send_money()



