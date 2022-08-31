# -*- coding: utf-8 -*-
# @time:         2022/8/29 21:08
# @Author:       Alan
# @File:         p1_function.py
# @Software:     PyCharm
# @Description:  学习函数

# todo 1.0 函数介绍
"""
一个Python语句块，它具有一个名称，可以作为一个语句组执行
函数是组织好，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。

使用函数
1. 定义函数 编写函数的名称和它包含的语句集合
2. 调用函数 执行函数中包含的语句集合

格式
def 函数名(形参列表):
    ...
    ...
    return 返回值

形参和实参
    - 定义函数时，指定的参数列表为形参列表
    - 执行函数时，传入的参数列表为实参列表

参数
- 必须参数
- 关键字参数
- 默认参数
- 不定长参数
"""


# todo 1.1 定义函数
# 定于一个名叫hello_world的函数
# 使用def关键字, 是define(定义)的缩写，后面指定函数的名称, 明后后面跟(), 里面可以写参数列表(形参),最后跟上:使用缩进编写要执行的代码块
def hello_world():
    print("Hello World!!!")
    print("可以重复使用的代码块~~~")
    print("===执行了hello_world函数===\n")


# todo 1.2 执行函数
# 调用函数; 一次定义可以多次调用
# 执行函数，使得函数内的所有语句都被执行
# 调用函数的语法: 函数名()
hello_world()
print("1")
hello_world()
print("2")
hello_world()
hello_world()


# todo 1.3 带参数的函数
# python 3.5 新特性 类型注解
# Python 运行时不强制执行函数和变量类型注解，但这些注解可用于类型检查器、IDE、静态检查器等第三方工具。
# 注解 变量: 数据类型
# 返回值类型 -> 数据类型
def sum1(a: int, b: int) -> int:
    return a + b


print(sum1(10, 15))
print("===带参数的函数===", end="\n\n")


# todo 1.4 传入不可变对象
# 调用函数前后，形参和实参指向的是同一个对象，而在函数内部修改值后，形参指向的是不同的id
# 值传递，不会改变原数据
def sub(a: int):
    print(f"修改前 形参a: {a}, a的id: {id(a)}")
    a -= 10
    print(f"修改后 形参a: {a}, a的id: {id(a)}")


a = 23
print(f"a的值: {a}\na的id: {id(a)}")
sub(a)
print(f"a的值: {a}\na的id: {id(a)}")
print("===传入不可变对象===", end="\n\n")


# todo 1.5 传入可变对象
# 传入可变对象时，对该对象进行的操作将影响原对象
# 值传递，传递的为地址
def app(x: list):
    x.append("abc")


alist = [1, 2, 3]
app(alist)
print(alist)
print("===传入可变对象===", end="\n\n")

# todo 1.6 参数
# todo 1.6.1 必需参数
# 不传入会报错： TypeError: app() missing 1 required positional argument: 'x'
# app()

# todo 1.6.2 关键字参数
# 使用形参=实参的形式来明确传入关系
# 使用关键字参数的时候，允许调用参数的顺序和声明时不一致
app(x=alist)
print(alist)
print(sum1(b=11, a=22))
print("===关键字参数===", end="\n\n")


# todo 1.6.3 默认参数
# 定义函数时可以指定默认参数
# 调用时，不指定该参数则使用默认参数
def printInfo(name: str, age: int = 15):
    print(f"我叫{name}, 今年{age}岁了!")


printInfo("alan")
print("===默认参数===", end="\n\n")


# 默认参数必须为最后一个参数
# def printInfo2(age: int = 15, name:str):
#     print(f"我叫{name}, 今年{age}岁了!")

# todo 1.6.4 不定长参数
# 有时不明确需要传递参数的个数，这是可以使用不定长参数
# 加了 * 的参数，会以元组的形式导入，存放所有未指定的变量
def printall(a: str, *args):
    print(a, args)
    print(type(args))


printall("a", "b", 1, 2, 3)


# 加 ** 的参数，会以字典的形式导入
def printall2(ab: str, **args):
    print(a, args)
    print(type(args))


printall2("ss", a=1, b=2, c=3)
print("===不定长参数===", end="\n\n")

# todo 1.7 return
# 用于退出函数。没有return的函数，返回None
print(printall2("ss", a=1, b=2, c=3))


def sum2(a, b):
    return a + b


print(sum2(1, 2))
print("===return===", end="\n\n")


# todo 1.8 强制位置参数
# Python 3.8新增函数形参语法 / 用来明确指明函数形参必须使用指定位置参数
#
def f(a, b, /, c, d, e):
    print(a, b, c, d, e)


# / 之前的参数，必须使用位置参数不能使用关键字参数
f(10, 20, c=30, e=40, d=50)
# f(a=10, 20, c=30, e=40, d=50)
f(10, 20, 30, 40, 50)
print("===强制位置参数===", end="\n\n")

# todo 1.9 匿名函数
# 使用lambda来创建匿名函数
# 格式 lambda 参数1,参数2,参数3,...:表达式
# 不再使用def语句定义
# lambda有自己的命名空间，不能访问自己参数列表或全局命名空间里的参数
# 也可以使用关键字参数和设定默认值
lambda1 = lambda x: x * x
print(lambda1(2))
print(lambda1(6))

lambda2 = lambda x, y: x + y
print(lambda2(4, 5))
print(lambda2(11, 22))
print("===lambda===", end="\n\n")
