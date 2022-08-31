# -*- coding: utf-8 -*-
# @time:         2022/8/30 16:20
# @Author:       Alan
# @File:         p2_reduce.py
# @Software:     PyCharm
# @Description:  reduce函数

"""
reduce() 接收两个参数，一个是函数，一个是Iterable
把一个函数作用在一个序列上，把结果继续和序列的下个元素做累积计算
将数据集合的值减少为单一结果

"""
from functools import reduce


def add(a, b):
    return a + b


aresult = reduce(add, [1, 2, 3, 4, 5])
print(aresult)

# 使用lambda表达式更加简洁
# reduce计算步骤
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
print(reduce(lambda a, b: a + b, range(100)))
print(reduce(max, range(10)))
