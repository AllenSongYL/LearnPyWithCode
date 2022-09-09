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
order 中的C从低纬度开始写，先写行，再写列，F从高纬度开始写

"""
import numpy
import numpy as np

# todo 1.0 创建数组
# todo 1.0.1 np.array创建数组
"""
np.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
返回类型numpy.ndarray
np.array(p_object: ndarray | Iterable | int | float,
           dtype: object | None = None,
#           *args: Any,
#           **kwargs: Any) -> ndarray
# p_object 数组或嵌套的数列
# dtype    数组元素的数据类型，可选
# copy     是否复制数组，可选
# order    排序方式，可选
# subok    是否返回子类型，可选
# ndmin    最小维度，可选
"""


a = np.array([1, 2, 3])
print(f"创建一个numpy数组: {a}, type: {type(a)}")

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"创建一个numpy二维数组: {b}\ntype: {type(b)}")

c = np.array([1, 2, 3], dtype=np.complex128)
print(f"创建一个numpy复数数组: {c}\ntype: {type(c)}")

d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("===array创建数组===", end="\n\n")

# todo 1.0.2 np.linspace创建数组
"""
在指定的时间间隔内返回均匀分布的数字。返回num 个均匀分布的样本，在区间 [ start , stop ] 上。
linspace() 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
np.linspace(start: float,
            stop: float,
            num: int = 50,
            endpoint: bool = True,
            retstep: bool = False,
            dtype: object | None = None,
            axis: int = 0) -> ndarray
            
# start     起始值
# stop      终止值
# num       要生成的等间隔样例数量，默认为50,必须为非负数。
# endpoint  终止值是否包含在样例内，默认为True
# retstep   如果为True，返回样例，以及连续数字之间的步长
# dtype     输出数组的类型
# axis      输出数组的形状，对于一维数组，不需要设置

，格式如下：
"""
one1 = np.linspace(1, 10, 10)
one2 = np.linspace(1, 10, 10, retstep=True)
print(one1)
print(one2)
print("===np.linspace创建均匀分布的一维数组===", end="\n\n")

# todo 1.0.3 np.arange创建数组
"""
在给定的间隔内返回均匀间隔的值。 类似于linspace，但使用步长（而不是样本数）。
当使用非整数步长时，例如 0.1，通常最好使用 numpy.linspace.
arange() 函数返回一个有终点和起点的固定步长的排列，格式如下：

np.arange(start, stop, step, dtype=None, *, like=None)
返回一个数组，其中包含从 start 到 stop（不包含 stop）按step步长组成的元素。
返回类型numpy.ndarray
np.arange(p_start: float,
                p_stop: float,
                p_step: float = 1,
                p_dtype: object | None = None) -> ndarray
# p_start  起始值
# p_stop   终止值
# p_step   步长
# p_dtype  输出数组的类型
"""

one2 = np.arange(0, 10, 5)
print(one2)
print("===np.arange创建指定步长的一维数组===", end="\n\n")

# todo 1.0.4 np.logspace创建数组
"""
在对数刻度上均匀分布的数字。返回num 个均匀分布的样本，在区间 [ start , stop ] 上。
logspace() 函数用于创建一个于等比数列。格式如下：
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)
np.logspace(start: float,
            stop: float,
            num: int = 50,
            endpoint: bool = True,
            base: float = 10.0,
            dtype: object | None = None,
            axis: int = 0) -> ndarray
# start     起始值是：base ** start
# stop      终止值是：base ** stop
# num       要生成的等间隔样例数量，默认为50,必须为非负数。
# endpoint  终止值是否包含在样例内，默认为True
# base      对数空间的底数，默认为10
# dtype     输出数组的类型
# axis      输出数组的形状，对于一维数组，不需要设置
"""
# 2为底数，则输出数组的元素为：2 ** 1, 10 ** 2, 10 ** 3, ..., 2 ** 9, 2 ** 10
one3 = np.logspace(1, 10, 10, base=2)
one4 = np.linspace(2**1, 2**10, 10)
print(one3, one4)
print("===np.logspace创建指定数量的等比数列===", end="\n\n")

# todo 1.0.5 np.eye创建数组
"""
eye() 函数用于创建一个对角线元素为1，其他元素为0的方阵。
格式如下：
np.eye(N, M=None, k=0, dtype=float, order='C')
np.eye(N, M=None, k=0, dtype=float, order='C')
返回一个 N 行 M 列的对角线元素为1，其他元素为0的方阵。
返回类型numpy.ndarray
np.eye(N: int,
        M: int = None,
        k: int = 0,
        dtype: object | None = None,
        order: str = 'C',
        *,
        like: Any = None) -> ndarray
# N      输出数组的行数
# M      输出数组的列数，默认为N 
# k      对角线元素的值，默认为0; 0表示主对角线，正值表示上对角线，负值表示下对角线。
# dtype  输出数组的类型
# order  输出数组的存储顺序，默认为C
# like   输出数组的格式，默认为None
"""

one5 = np.eye(3)
print(one5)
print("===np.eye创建对角线元素为1，其他元素为0的方阵===", end="\n\n")

# todo 1.0.6 np.diag创建数组
"""
diag() 函数用于创建一个对角线元素为1，其他元素为0的方阵。
格式如下：
np.diag(v, k=0)

np.diag(v: array_like,
        k: int = 0) -> ndarray
v  类数组；如果是二维数组，则返回其第k个对角线元素的对角线元素组成的数组；
          如果是一维数组，则返回其对角线元素组成的数组。
k 对角线元素的值，默认为0; 0表示主对角线，正值表示上对角线，负值表示下对角线。
                  
返回一个 N 行 M 列的对角线元素为1，其他元素为0的方阵。
返回类型numpy.ndarray
"""

one6 = np.diag([1, 2, 3])
print(one6)
print("===np.diag创建对角线元素为1，其他元素为0的方阵===", end="\n\n")

# todo 1.0.7 np.ones创建数组
"""
ones() 函数用于创建一个具有指定维度的，元素全部为1的数组。
格式如下：
np.ones(shape, dtype=float, order='C')
返回一个 shape 的数组，数组元素全部为1。
返回类型numpy.ndarray
np.ones(shape:  int | Iterable[int],
        dtype: object | None = None,
        order: str | None = 'C',
        *,
        like: Any = None) -> ndarray
shape  数组的形状
dtype  数组的类型,默认 numpy.float64
order  数组的存储顺序，默认为C
like  数组的格式，默认为None

numpy.zeros(shape, dtype=float, order='C')
和ones()函数类似，只不过是元素全部为0。

numpy.empty(shape, dtype=float, order='C')
和ones()函数类似，只不过是元素不初始化。
empty与 不同zeros，它不会将数组值设置为零，因此可能会稍微快一些。

numpy.full(shape, fill_value, dtype=None, order='C')
和ones()函数类似，只不过是元素全部为fill_value。
fill_value  填充数组元素的值

numpy.full_like(a, fill_value, dtype=None, order='K', subok=True, shape=None)
和ones()函数类似，只不过是元素全部为fill_value。
a  用于确定形状和类型的参考数组
fill_value  填充数组元素的值

"""

# todo 1.0.8 创建三维数组
# 5列4行，3个组成 3维数组
print(f"np.ones((3, 4, 5)) = {np.ones((3, 4, 5))}", end="\n")
print(f"np.zeros((3, 4), dtype=np.int32) = {np.zeros((3, 4), dtype=np.int32)}", end="\n")
print(f"np.empty((2, 3)) = {np.empty((2, 3))}", end="\n")
print(f"np.full((2, 3), 7) = {np.full((2, 3), 7)}", end="\n")
print(f"numpy.full_like(one7, 8) = {numpy.full_like(one6, 8)}", end="\n")
print("===np.ones/zeros/empty/full/full_like创建具有指定维度的，元素全部为1的数组===", end="\n\n")


# todo 1.1 属性
# ndim 属性返回数组的维数
print(a.ndim, b.ndim, type(a.ndim))

# shape 属性返回一个包含数组维度的元组
# (行, 列)
print(a.shape, b.shape, type(a.shape))

# size 属性返回数组中的元素个数
# 行 * 列
print(a.size, b.size, type(a.size))

# dtype 属性返回数组中元素的数据类型
print(a.dtype, b.dtype, type(a.dtype))

# itemsize 属性返回数组中每个元素的字节单位长度
print(a.itemsize, b.itemsize, type(a.itemsize))

# nbytes 属性返回数组中所有元素的字节单位长度
# size * itemsize = nbytes 每个元素的字节长度 * 元素个数 = 总字节长度
print(a.nbytes, b.nbytes, type(a.nbytes))

