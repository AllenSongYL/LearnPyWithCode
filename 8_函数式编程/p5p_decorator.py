# -*- coding: utf-8 -*-
# @time:         2022/8/30 9:34
# @Author:       Alan
# @File:         p5p_decorator.py
# @Software:     PyCharm
# @Description:  Python 装饰器

# todo 1.0 装饰器
"""
最常用的高阶函数
允许我们包装另一个函数，以扩展包装函数的行为，而无需永久修改它
"""
import time


def decorator_function(oldFcuntion):
    def newFunction():
        print(f"装饰器执行 {oldFcuntion.__name__}")
        oldFcuntion()
        print("decorator_function修饰结束!")

    return newFunction


# 相当于 decorator_function(test)
@decorator_function
def test():
    print("test function")


test()
print("===无参装饰器===", end="\n\n")


# todo 1.1 装饰带参数的函数
def df(oldFcuntion):
    def newFunction(name):
        print(f"装饰器执行 {oldFcuntion.__name__} 函数")
        oldFcuntion(name.upper())
        oldFcuntion(name[::-1])
        print("修饰结束!")

    return newFunction


@df
def test2(name):
    print(f"hello {name}")


test2('alan')
print("===装饰带参数的函数===", end="\n\n")


# todo 1.2 计时装饰器案例
def df2(oldFcuntion):
    def newFunction(n, m):
        tStart = time.time()
        all = oldFcuntion(n, m)
        print("oldFcuntion")
        tEnd = time.time()
        print(f"修饰结束!运行时长: {tEnd - tStart}")
        return all

    return newFunction


@df2
def test3(n, m):
    count = 0
    for i in range(n, m):
        count += i
    return count


print(test3(1, 100))
print("===计时装饰器===", end="\n\n")


# todo 1.3 多装饰
# 使用多个装饰器
# 就近元组，先运行最近的装饰器
def dcf(oldFcuntion):
    def newFunction():
        oldFcuntion()
        oldFcuntion()
        print("dcf装饰器， 运行2遍")

    return newFunction


@dcf
@decorator_function
def multtest():
    print("使用多个装饰器")


multtest()
print("===多装饰器===", end="\n\n")


# todo 1.4 带参数装饰器
#
def decorator(para):
    if para == 'double':
        def func1(fn):
            fn()
            fn()
            print("装饰器1运行")

        return func1
    elif para == 'three':
        def func2(fn):
            fn()
            fn()
            fn()
            print("装饰器2运行")

        return func2
    else:
        def func3(fn):
            fn()
            print("装饰器3运行")

        return func3


@decorator('double')
def h1():
    print("hi h1~~~")


@decorator('three')
def h2():
    print("hi h2")


h1()
print("===")
h2()
