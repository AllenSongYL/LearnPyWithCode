# -*- coding: utf-8 -*-
# @time:         2022/9/5 22:02
# @Author:       Alan
# @File:         p10_3.10.py
# @Software:     PyCharm
# @Description:

# todo 1.0 bin_count函数
# 统计二级制中数字1的个数
value = 5
print(value.bit_count())

# todo 1.1 联合运算符
# 在之前的 Python 版本中，要为可接受多种类型参数的函数应用类型提示，使用的是 typing.Union
# 但是在 Python 3.10 中，可以使用 | 运算符来实现
# def square(number: int | float) -> int | float:

# todo 1.2 字典keys,value,items方法新增一个mapping属性
#  ，返回一个字典视图对象
a = {"name": "alan", "age": 18}
b = a.keys()
print(b.mapping, type(b.mapping), b.mapping["age"])

# todo 1.3 zip添加stict参数，当参数长度不一致时，抛出异常
#  默认为False
a = [1, 2, 3]
b = [4, 5, 6, 7]
c = zip(a, b, strict=True)
print(c)

# todo 1.4 结构化模式匹配
# match...case...语句
# 语法：
# match <expression>:
#     case <pattern>:
#         <statement>
#     case <pattern>:
#         <statement>
#     case <pattern>:
#         <statement>
#     case _:
#         <statement>
# 说明：
# 1. match语句的表达式可以是任何表达式，但是必须是常量表达式
# 2. case语句的模式可以是任何表达式，但是必须是常量表达式


