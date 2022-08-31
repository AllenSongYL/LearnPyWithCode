# -*- coding: utf-8 -*-
# @time:         2022/8/29 20:44
# @Author:       Alan
# @File:         lazy.py
# @Software:     PyCharm
# @Description:  惰性求值

"""
生成器对象不会计算和产生素有结果，，除非客户端代码请求这些结果。
"""
import random

# todo 1.1 惰性求值 如：map函数,range函数,filter函数
num1 = [1, 2, 3, 4]
map1 = map(print, num1)
print(map1)
print("===")
print(list(map1))


# 以上会产生[None, None, None, None]
# 原因: list转换时，需要遍历map结果，强制它自行求值，这回使每个元素调用print。
#      因为print没有返回值，所以输出None

# todo 1.2 使用yield
# 调用函数不会直接无限循环，只有在next()函数，才会从序列中取出单个值
# 可以创建潜在的包含大量值或无限值的生成器对象，除了客户端实际使用的值之外，不需要为此类对象消耗计算机资源
def int_rand_seq(min, max):
    while True:
        yield random.randint(min, max)


a1 = int_rand_seq(0, 10)
print(a1)
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))

