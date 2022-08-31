# -*- coding: utf-8 -*-
# @time:         2022/8/29 21:03
# @Author:       Alan
# @File:         p1_map.py
# @Software:     PyCharm
# @Description:  map函数

"""
将函数应用于数据集合的每个元素，并生成新的数据集合的函数式操作

map()接收两个参数，一个是函数，一个是Iterable
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
配合lambda匿名函数，可以大大简化代码
返回的是一个可迭代的数据集合不是列表，而是一个迭代器，可以使用list()函数转换为列表
map产生的的结果和原始数据集合的长度总是相同的
"""


def way(x):
    return x ** x


resulta = map(way, [1, 2, 3, 4, 5, 6])
print(resulta)
for i in resulta:
    print(i)

print("===map普通函数===", end="\n\n")

num1 = [7, 8, 9, 10]
print(sum(map(lambda n: n * n, num1)))
print("===map匿名函数===", end="\n\n")
