# -*- coding: utf-8 -*-
# @time:         2022/8/29 16:44
# @Author:       Alan
# @File:         gentrator.py
# @Software:     PyCharm
# @Description:  迭代器和生成器

# todo 1.0 迭代器
"""
迭代器（iterator）就是一个封装了迭代的对象。
迭代器和生成器都是为了惰性求值（lazy evaluation），避免浪费内存空间，实现高效处理大量数据。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
一个对象有__next__()方法
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器.

迭代器用于支持：
for 循环
构建和扩展集合类型
逐行遍历文本文件
列表推导、字典推导和集合推导
元组拆包
调用函数时，使用 * 拆包实参

总结下，迭代器的特点：

惰性：迭代器并不是把所有的元素提前计算出来，而是在需要的时候才计算返回。
支持无限个元素：它创建是一个规则，由于是惰性的，你永远可能不会把所有元素全部使用，而列表等容器没法容纳无限个元素的
节省空间：迭代器惰性的特点，存储的是规则算法，因此不会占用太多内存
迭代器同时也是可迭代对象
迭代器遍历完一次就不能从头开始了，用完即销毁，对项的使用是「一次性」的【重点注意】
"""

# todo 1.1 创建迭代器
list1 = [1, 2, 3, 4]
it = iter(list1)
print(f"{it}, {type(it)}")
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# 超过会报错 StopIteration
# print(next(it))
print("===迭代器 next===", end="\n\n")

it2 = iter(list1)
# 本质上 for 循环就是不断地调用迭代器的next方法）
for i in it2:
    print(i)
print("===迭代器 for===", end="\n\n")

# todo 1.2 生成器
"""
生成器是特殊的迭代器，它也是一种更简单的创建迭代器的方法。
它的功能本质是创建了一个规则，但只有在迭代使用时才产生值（当然迭代器的思想也是这样），
而不是一次构建完整的列表。生成器类型是这个思想的最佳践行。

使用了 yield 的函数被称为生成器（generator）
生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
调用一个生成器函数，返回的是一个迭代器对象。

Python 中，提供了两种 生成器（Generator） ，一种是生成器函数，另一种是生成器表达式。
生成器函数，定义与常规函数相同，区别在于，它使用 yield 语句 而不是 return 语句 返回结果
生成器表达式，与列表推导式类似，区别在于，它使用小括号 () 包裹
"""


# todo 1.2.1 生成器函数
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            raise StopIteration
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
print(f, type(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print("===生成器函数===", end="\n\n")

# todo 1.2.2 生成器表达式
"""
生成器表达式，与列表推导式类似，区别在于，它使用小括号 () 包裹
"""
gen_exp = (x * 2 for x in range(10))
# gen_exp = iter(range(10))
print(gen_exp, type(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print("===生成器表达式===", end="\n\n")
