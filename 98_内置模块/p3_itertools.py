# -*- coding: utf-8 -*-
# @time:         2022/8/30 8:17
# @Author:       Alan
# @File:         p3_itertools.py
# @Software:     PyCharm
# @Description:  itertools

import itertools

# todo 1.0 itertools介绍
"""
该模块标准化了一组核心的快速、高效的内存工具，这些工具本身或组合使用。
它们一起形成了一个“迭代器代数”，使得在纯 Python 中简洁有效地构建专用工具成为可能。
"""

# todo 1.1 无限迭代器
# todo 1.1.1 count()
# 创建一个迭代器，从start开始，每次增加step，无限循环
# 它返回以数字start 开头的均匀间隔的值。
# 通常用作map()生成连续数据点的参数。此外，用于zip()添加序列号。
foo = itertools.count(start=0, step=1)
print(foo, type(foo))

# 无限循环
# for i in foo:
#     print(i)

# todo 1.1.2 cycle()
# 制作一个迭代器，从可迭代对象中返回元素并保存每个元素的副本。
# 当迭代耗尽时，从保存的副本中返回元素。无限重复。
foo2 = itertools.cycle(['a', 'b', 'c'])
print(foo2, type(foo2))
print(next(foo2))
print(next(foo2))
print(next(foo2))
print(next(foo2))
print(next(foo2))

# todo 1.1.3 repeat()
# 创建一个迭代器，从可迭代对象中返回元素，并重复指定次数。
foo3 = itertools.repeat('a', 3)
print(foo3, type(foo3))
print(next(foo3))
print(next(foo3))
print(next(foo3))

# todo 1.2 终止于最短输入序列的迭代器
# todo 1.2.4 takewhile()
# 创建一个迭代器，从可迭代对象中返回元素，直到某个条件不满足。
foo4 = itertools.takewhile(lambda x: x < 3, [1, 2, 3, 4, 5])
print(foo4, type(foo4))
print(next(foo4))
print(next(foo4))
# 再取出会报错，因为已经没有元素了 StopIteration
# print(next(foo4))
