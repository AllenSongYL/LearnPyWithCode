# -*- coding: utf-8 -*-
# @time:         2022/8/29 16:15
# @Author:       Alan
# @File:         p2_while.py
# @Software:     PyCharm
# @Description:  while循环

# todo 1.0 while 循环
"""
while 判断条件：
    执行语句

判断条件为真，则执行代码块中的语句，否则退出while循环
"""

a = 0
while a < 10:
    print(a)
    a += 1


# todo 1.1 无限循环
while True:
    print("无限循环...")
