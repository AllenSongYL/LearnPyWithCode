# -*- coding: utf-8 -*-
# @time:         2022/8/30 9:12
# @Author:       Alan
# @File:         higher_function.py
# @Software:     PyCharm
# @Description:  高阶函数

# todo 1.0 高阶函数
"""
函数是对象类型（Object type）的实例
可以将函数存储在变量中
可以将函数作为参数传递给另一个函数
可以从函数返回函数
可以将它们存储在数据结构中，如哈希表、列表等…

"""


# todo 1.0 函数作为对象
# 可以将函数分配给变量，此赋值不调用函数，而是创建对该函数的引用。
def printline(n):
    print(f'---{n}---')


printline("Hello World")
# 将函数存储在变量中
newprint = printline
newprint("Hello World222")


# todo 1.1 函数作为参数传递
def pp(fc):
    """
    函数作为参数传递给另一个函数
    :param fc: 传入一个函数，调用函数
    :return: None
    """
    fc("aaa")
    print("bbb")


pp(printline)

# todo 1.2 返回函数
# 由于函数是对象也可以从另一个函数返回一个函数
def create_adder(x):
    def adder(y):
        return x + y
    return adder


add_10 = create_adder(10)
print(add_10)
print(add_10(15))

# todo 1.3 闭包
# 闭包是一个函数，它持有一个变量的引用，这个变量可能是一个函数，也可能是一个变量。