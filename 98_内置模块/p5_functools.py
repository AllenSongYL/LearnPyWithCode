# -*- coding: utf-8 -*-
# @time:         2022/8/30 16:24
# @Author:       Alan
# @File:         p5_functools.py
# @Software:     PyCharm
# @Description:  functools模块

"""
应用于高阶函数，即参数或返回值为其他函数的函数。

"""

import functools

# todo 1.0 wraps()
"""
便捷函数，用于在定义包装器函数时，发起调用update_wrapper()函数，更新包装器函数的__doc__和__name__属性。
partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)

如果不使用这个装饰器工厂函数，则 example 函数的名称将变为 'wrapper'，
并且 example() 原本的文档字符串将会丢失。
"""


def my_decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)

    return wrapper


@my_decorator
def example():
    """Docstring"""
    print("Called example function")


example()
print(example.__name__)  # 不使用wraps:返回wrapper 使用wraps:返回example
print(example.__doc__)  # 不使用wraps:返回None  使用wraps:返回Docstring
print("===wraps()===", end="\n\n")

# todo 1.1 partial(func, /, [*args,] [**kwargs])
"""
把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
partial() 会被“冻结了”一部分函数参数和/或关键字的部分函数应用所使用，从而得到一个具有简化签名的新对象。

使用场景
写一个参数较多的函数，大部分场景下都是某个固定值，为了简化使用，就可以创建一个新函数
指定要使用的函数的某个参数，为某个固定的值，这个新函数就是偏函数。
只需要传入一部分参数，可以使用 partial 函数来实现。
"""


def test(a, b, c):
    print(a, b, c)


# 使用偏函数，指定c的默认值为3,只需要传入a和b的值；
# 返回一个新的函数，这个新函数可以接受任意数量的参数，但只需要传入a和b的值，c的值默认为3
test2 = functools.partial(test, c=3)
test2(1, 2)
# 这时候如果传递了c的值，TypeError: test() got multiple values for argument 'c'
# test2(1, 2, 3)
print("===partial()===", end="\n\n")

# todo 1.3 singledispatch()
"""
singledispatch()函数是一个装饰器，用于实现单个dispatch的功能。
实现java中重载的功能。
将一个函数转换为 单分派 generic function，即可以接受不同的参数，但只会调用一个函数。
要定义一个泛型函数，用装饰器 @singledispatch 来装饰它。
当使用 @singledispatch 定义一个函数时，请注意调度发生在第一个参数的类型上
要将重载的实现添加到函数中，请使用泛型函数的 register() 属性，它可以被用作装饰器。
对于不使用类型标注的代码，可以将适当的类型参数显式地传给装饰器本身register(int)
"""


@functools.singledispatch
def func(args):
    print(args)


@func.register(int)
def _(arg: int):
    print("int类型~")


@func.register(str)
def _(arg: str):
    print("str类型~")


@func.register(list)
def _(arg: list):
    print("list类型~")


#
func.register(type(None), lambda arg: print("None类型~"))

func(1)
func("a")
func([1, 2, 3])
func(None)
print("===singledispatch()===", end="\n\n")

# todo 1.4 singledispatchmethod(func)
"""
要定义一个泛型方法，用装饰器 @singledispatchmethod 来装饰它。
当使用 @singledispatchmethod 定义一个函数时，请注意发送操作将针对第一个非 self 或非 cls 参数的类型上。
"""


class Negator:
    @functools.singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg

    @neg.register(str)
    def _(self, arg: str):
        return "".join(reversed(arg))


aNegetor = Negator()
print(aNegetor.neg(1))
print(aNegetor.neg(True))
print(aNegetor.neg("abcdefg"))
