# -*- coding: utf-8 -*-
# @time:         2022/8/30 6:19
# @Author:       Alan
# @File:         p5_3.5.py
# @Software:     PyCharm
# @Description:  python 3.5新特性
import os
import typing
import numpy as np
import asyncio

# todo 1.0 typing 函数类型注解支持
"""
PEP 484 引入了函数形参类型标注即类型提示的标准
注解 Python 运行时不强制执行函数和变量类型注解，但这些注解可用于类型检查器、IDE、静态检查器等第三方工具。
注解 变量: 数据类型
返回值类型 -> 数据类型
"""


def greeting(name: str) -> str:
    return f'Hello {name}'


print("===函数使用类型注解===", end="\n\n")

# todo 1.0.1 类型别名
# 适用于简化复杂的类型签名
Vector = list[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)
print("===类型别名===", end="\n\n")

# todo 1.0.2 新建类型
UserId = typing.NewType('UserId', int)
some_id = UserId(524313)


def get_user_name(user_id: UserId) -> str:
    ...


print("===新建自定义类型===", end="\n\n")

# todo 1.2 async和await
"""
    PEP 492 - 使用 async 和 await 语法实现协程
    在协程函数内部，新await表达式可用于暂停协程执行，直到结果可用。
    任何对象都可以被等待，只要它通过定义方法实现了等待协议。__await__()
    还添加了对异步可迭代对象进行方便迭代的语句。async for
"""


async def main():
    print("Hello World")
    # asyncio.sleep是一个协程，应该等待。
    await asyncio.sleep(1)
    print("Hello Again")


asyncio.run(main())
print("===async和await===", end="\n\n")

# todo 1.3 @ 运算符
# PEP465 用于矩阵乘法的专用中缀运算符 @
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print(f"x @ y = {x @ y}")
print("===@运算符===", end="\n\n")

# todo 1.4 *和**
# PEP 448 - 额外的解包
# 在 3.5 之前，函数调用时，一个函数中解包操作只允许一个 * 和一个 **
# 3.5+ 之后，可以有任意多个解包
# 扩展了*可迭代解包运算符和**字典解包运算符的允许用途。现在可以在函数调用中使用任意数量的解包
# 解包: 将可迭代对象解包为一个元组 变量数不等于右侧可迭代对象中元素的个数时，会抛出异常
print([1, 2, 3, 4])
print(*[1, 2, 3, 4])
print(*[1, 2, 3, 4], sep=",")
a, b, c = [1, 2, 3]
print(f"a, b, c = [1, 2, 3] 解包: {a, b, c}")

# 用解包的方式获得中间的数值  变量数不等于右侧可迭代对象中元素的个数时,可以使用*接收多个
first, *new, last = [94, 85, 73, 46]
print(new)

# TypeError: 'a' is an invalid keyword argument for print()
# print(**{'a': 1, 'b': 2, 'c': 3})
print({"a": 1, **{"b": 2, "c": 3}})
print("===*和**===", end="\n\n")

# todo 1.5 os.scandir()
# PEP 471 - 新的 os.scandir() 函数
# 使其在 POSIX 系统上快 3 到 5 倍，在 Windows 系统上快 7 到 20 倍。
# scandir返回一个迭代器，而不是返回一个文件名列表，这在迭代非常大的目录时提高了内存效率
# 返回一个 os.DirEntry 对象的迭代器，它们对应于由 path 指定目录中的条目。 这些条目会以任意顺序生成，并且不包括特殊条目 '.' 和 '..'。
# scandir.close() 关闭迭代器并释放占用的资源
# 当迭代器迭代完毕，或垃圾回收，或迭代过程出错时，将自动调用本方法。但仍建议显式调用它或使用 with 语句
for i in os.scandir("."):
    print(i.name)