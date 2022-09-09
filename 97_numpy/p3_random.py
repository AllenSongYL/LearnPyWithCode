# -*- coding: utf-8 -*-
# @time:         2022/8/31 20:57
# @Author:       Alan
# @File:         p3_random.py
# @Software:     PyCharm
# @Description:  numpy.random

import numpy as np
# todo 1.0 np.random.random()
# random_sample 的别名，用于轻松向前移植到新的随机 API。
# 指定形状产生一个[0.0,1.0)之间的随机浮点数
# 仅支持一个参数，即形状
# 如果只指定一个数字，则产生一个一维数组
# 如果指定一个shape元组(2, 5)，则产生指定形状的数组

print(f"random.random(): {np.random.random()}")
print(f"random.random((2, 4)): {np.random.random((2, 4))}")
print(f"random.random([2, 4]): {np.random.random([2, 4])}")
print("===np.random.random()===", end="\n\n")

# todo 1.1 np.random.rand()
# 指定形状产生一个[0,1)之间的随机浮点数
# 可以传入多个参数
print(f"random.rand(): {np.random.rand()}")
print(f"random.rand(2, 4): {np.random.rand(2, 4)}")
print("===np.random.rand()===", end="\n\n")

# todo 1.2 np.random.randint()
# 产生指定范围内的随机整数
# 可以传入多个参数
# def randint(low: int | ndarray | Iterable | float[int],
#             high: int | ndarray | Iterable | float[int] | None = None,
#             size: int | Iterable | tuple[int] | None = None,
#             dtype: object | None = None) -> int
# 参数：
# low:  产生随机数的下限
# high:  产生随机数的上限
# size:  产生随机数的形状,当size为整数时，产生的随机数为一维数组；当size为元组时，产生的随机数为多维数组
# dtype:  产生随机数的数据类型 只能是int或者int32这种类型
# 返回值：
# int 产生的随机数
print(f"random.randint(1, 10): {np.random.randint(1, 10)}")

# todo 1.3 np.random.choice()
"""
从给定的一维数组中生成随机数
def choice(a: Any,
           size: int | Iterable | tuple[int] | None = None,
           replace: bool | None = True,
           p: Any = None) -> Any
参数：
a:  一维数组
size:  产生随机数的形状,当size为整数时，产生的随机数为一维数组；当size为元组时，产生的随机数为多维数组
replace:  是否可以重复抽取,默认为True
p:  每个元素被抽取的概率
返回值：
int 产生的随机数
"""

print(f"random.choice([1, 2, 3, 4, 5]): {np.random.choice([1, 2, 3, 4, 5])}")
print(f"random.choice([1, 2, 3, 4, 5]): {np.random.choice([1, 2, 3, 4, 5], size=(2, 3), p=[0.1, 0.2, 0.3, 0.2, 0.2])}")
print("===np.random.choice()===", end="\n\n")

# todo 1.4 np.random.shuffle()
"""
将数组中的元素随机打乱, 会改变原数组
def shuffle(x: Any) -> None
参数：
x:  一维数组
返回值：
None
"""
a = np.arange(10)
print(a)
np.random.shuffle(a)
print(f"random.shuffle(a): {a}")
print("===np.random.shuffle()===", end="\n\n")

# todo 1.5 np.random.permutation()
"""
将数组中的元素随机打乱, 不会改变原数组
def permutation(x: Any) -> Any
参数：
x:  一维数组
返回值：
None
"""
b = np.arange(10)
print(b)
print(f"random.permutation(b): {np.random.permutation(b)}")
print(b)
print("===np.random.permutation()===", end="\n\n")

# todo 1.6 np.random.random_sample()
"""
产生指定形状的[0,1)之间的随机浮点数
def random_sample(size: int | Iterable | tuple[int] | None = None) -> float
参数：
size:  产生随机数的形状,当size为整数时，产生的随机数为一维数组；当size为元组时，产生的随机数为多维数组
返回值：
float 产生的随机数
"""
print(f"random.random_sample(): {np.random.random_sample()}")
print(f"random.random_sample((2, 3)): {np.random.random_sample((2, 3))}")
print("===np.random.random_sample()===", end="\n\n")

# todo 1.7 np.random.randn()
"""
产生指定形状的标准正态分布的随机浮点数
def randn(d0: int | None = None,
            d1: int | None = None,
            d2: int | None = None,
            ...,
            dn: int | None = None) -> float
    参数：
    d0-dn:  产生随机数的形状
    返回值：
    float 产生的随机数
"""
print(f"random.randn(): {np.random.randn()}")
print(f"random.randn(): {np.random.randn(5)}")
