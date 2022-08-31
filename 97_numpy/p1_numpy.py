# -*- coding: utf-8 -*-
# @time:         2022/8/31 14:24
# @Author:       Alan
# @File:         p1_numpy.py
# @Software:     PyCharm
# @Description:  学习使用numpy

"""
一个开源 Python 库,它是在 Python 中处理数值数据的通用标准库
NumPy 库包含多维数组和矩阵数据结构，以及相关的运算工具

ndarray 对象是用于存放同类型元素的多维数组。
ndarray 中的每个元素在内存中都有相同存储大小的区域。
ndarray 内部由以下内容组成
    - 一个指向数据（内存或内存映射文件中的一块数据）的指针。
    - 数据类型或 dtype，描述在数组中的固定大小值的格子。
    - 一个表示数组形状（shape）的元组，表示各维度大小的元组。
    - 一个跨度元组（stride），其中的整数指的是为了前进到当前维度下一个元素需要"跨过"的字节数。

Python 列表和 NumPy 数组有什么区别？
NumPy 为您提供了大量快速有效的方法来创建数组和操作其中的数值数据。
虽然 Python 列表可以在单个列表中包含不同的数据类型，但 NumPy 数组中的所有元素都应该是同质的。
如果数组不是同质的，则打算在数组上执行的数学运算将非常低效。

为什么要使用 NumPy？
NumPy 数组比 Python 列表更快、更紧凑。数组占用内存少，使用方便。
NumPy 使用更少的内存来存储数据，它提供了一种指定数据类型的机制。这允许进一步优化代码。

NumPy 中的索引从 0 开始
"""

import numpy as np

# todo 1.0 创建一个numpy数组
# 返回类型numpy.ndarray
# np.array(p_object: ndarray | Iterable | int | float,
#           dtype: object | None = None,
#           *args: Any,
#           **kwargs: Any) -> ndarray
# p_object 数组或嵌套的数列
# dtype    数组元素的数据类型，可选
# copy     是否复制数组，可选
# order    排序方式，可选
# subok    是否返回子类型，可选
# ndmin    最小维度，可选

a = np.array([1, 2, 3])
print(f"创建一个numpy数组: {a}, type: {type(a)}")

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"创建一个numpy二维数组: {b}\ntype: {type(b)}")

c = np.array([1, 2, 3], dtype=np.complex128)
print(f"创建一个numpy复数数组: {c}\ntype: {type(c)}")

print("===array创建数组===", end="\n\n")


# 通过索引访问数组中的元素
print(a[0])
print(b[0][3])