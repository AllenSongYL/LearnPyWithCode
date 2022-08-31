# -*- coding: utf-8 -*-
# @time:         2022/8/30 16:35
# @Author:       Alan
# @File:         p3_filter.py
# @Software:     PyCharm
# @Description:  filter函数

"""
作用于数据集合，将新数据集合限制为通过了某些判断的值
将布尔函数应用于数据集合中的每个元素的函数式操作
保留函数返回值为True的元素，丢弃返回值为False的元素
"""

aresult = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(aresult)
for i in aresult:
    print(i)
