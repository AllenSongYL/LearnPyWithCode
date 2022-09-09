# -*- coding: utf-8 -*-
# @time:         2022/8/31 21:51
# @Author:       Alan
# @File:         p4_index.py
# @Software:     PyCharm
# @Description:  NumPy 索引和切片

import numpy as np

"""
ndarray对象的内容可以通过索引来访问，索引可以是整数，整数数组，或者是布尔数组。
"""

# todo 1.0 通过索引访问数组中的元素
a = np.arange(10)
b = np.random.randint(0, 10, (3, 4))

print(f"a: {a}, a[0]: {a[0]}")
print(f"b: {b}, b[0][2]: {b[0][2]}")
print("===通过索引访问数组中的元素===", end="\n\n")

# todo 1.1 切片
print(f"a[1:5]: {a[1:9:2]}")
print(f"a: {a}, a[2:]: {a[2:]}")
print(f"a: {a}, a[2::2]: {a[2::2]}")
print(f"b: {b}, b[1:]: {b[1:]}")
print(f"b: {b}, b[1::2]: {b[1::2]}")
print(f"b: {b}, b[..., 1]: {b[..., 1]}")  # ...表示所有行，所有列，第二列
print(f"b: {b}, b[..., 2]: {b[..., 2]}")  # ...表示所有行，所有列，第三列
print(f"b: {b}, b[2, ...]: {b[2, ...]}")  # 第二行，所有列
print(f"b: {b}, b[2, ..., 1]: {b[2, ..., 1]}")  # 第二行，所有列，第二列
print(f"b: {b}, b[...,1:]: {b[...,1:]}")  # 所有行，第二列到最后一列
# 多维数组的切片，可以使用下标来指定每一维的范围
# 如果只指定一个整数，则表示该维的全部元素
# 使用,号分隔多个索引，表示多个维度的切片
print(f"b: {b}, b[0:2,0:2]: {b[0:2,0:2]}") # 第一行到第二行，第一列到第二列
# 也可以使用slice函数，slice(start, stop, step)
# 这种方式是为了以后多次调用
aslice = slice(1, 9, 2)
print(f"a[aslice]: {a[aslice]}")
