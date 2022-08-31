# -*- coding: utf-8 -*-
# @time:         2022/8/30 6:36
# @Author:       Alan
# @File:         p6_3.6.py
# @Software:     PyCharm
# @Description:  Python 3.6 新特性
import asyncio
import typing

# todo 1.0 格式化字符串
# PEP 498 格式化字符串字面值
name = "Alan"
age = 18
# 旧格式化字符串
print("我叫%s,今年%d岁" % (name, age))
# 新格式化字符串
print(f"我叫{name},今年{age}岁")
print("===使用类型注解===", end="\n\n")

# todo 1.1 数字字面值中"_"
# PEP 515 数字字面值中的下划线
# 增加了在数字字面值中使用下划线的能力以改善可读性。
# 单个下划线允许用在数码之间和任何数制指示符之后。 一行内不允许有开头、末尾或多个下划线。
print(1_000_000_000_000_000)
print(0x_FF_FF_FF_FF)

print("===_===", end="\n\n")

# todo 1.2 变量标注
# PEP 526 变量标注的新特性

age: int = 25
l1: typing.List = [1, 2, 3]
s1: typing.Set = {1, 2, 3}
d1: typing.Dict = {'a': 1, 'b': 2}
t1: typing.Tuple = (1, 2, 3)
t2: typing.Tuple[int, str] = (1, 'a')
maybe_none: typing.Optional[str] = None


# todo 1.3 异步生成器
# PEP 492 异步生成器的新特性
# Python 3.5 实现的一个明显限制是不可能在同一函数体中同时使用 await 和 yield。
# 在 Python 3.6 中此限制已被解除，这样就就能够定义 异步生成器

async def ticker(to):
    """产生从 0 到 to delay延迟秒数的数字。"""
    for i in range(to):
        yield i
        await asyncio.sleep(0.5)


# todo 1.4 异步推导式
# 添加了对在列表、集合与字典推导式和生成器表达式中使用 async for 的支持

result = [i async for i in ticker(10) if i % 2 == 0]
print(result)
