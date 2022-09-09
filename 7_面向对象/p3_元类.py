# -*- coding: utf-8 -*-
# @time:         2022/9/8 13:56
# @Author:       Alan
# @File:         p3_元类.py
# @Software:     PyCharm
# @Description:  元类

"""
元类
1. 创建类的类
2. 元类是类的模板
3. 类是元类的实例

type是python的内置元类

type创建类的过程
type(name, bases, attrs)
    name: 类名
    bases: 父类的元组（用于继承，可以为空）
    attrs: 包含属性名称和值的字典


"""


# 继承元类type
# 元类One
class One(type):
    # new方法是创建实例的方法
    def __new__(cls, name, bases, dicts):
        print(f"元类One; __new__构造方法, 创建对象: {name} 父类: {bases} 属性: {dicts}")
        # 可以写成
        # return super().__new__(cls, name, bases, dicts)
        # 调用父类type的__new__方法，创建类
        new_cls = type.__new__(cls, name, bases, dicts)
        print(f"__new__返回类: {new_cls}")
        return new_cls

    # init方法是初始化实例的方法
    def __init__(self, name, bases, dicts):
        print(f"元类One; __init__初始化方法, 初始化对象: {name} 父类: {bases} 属性: {dicts}")
        # 调用父类type的__init__方法，初始化类
        # super().__init__(name, bases, dicts)
        type.__init__(self, name, bases, dicts)

    # call方法是调用实例的方法
    # 通过类名()调用类时，会调用call方法
    def __call__(self, name, bases, dicts):
        print(f"元类One; __call__调用方法, 调用对象:  {name}")
        self.__new__(name, bases, dicts)
        self.__init__(name, bases, dicts)


# 创建类，指定元类One
# Two类由One元类创建
# 调用One的__new__方法，返回Two类
# 调用One的__init__方法，初始化Two类
class Two(metaclass=One):
    pass


# Two类其实是One类创建的实例对象
print(f"通过class关键字创建Two类: {Two} 由 {Two.__class__} 创建\n")

# 通过type元类创建类，实例化对象Three
# 实际是使用type的__call__方法
# __call__方法调用__new__方法，返回Three类
# __call__方法调用__init__方法，初始化Three类
Three = type("Three", (object,), {})
print(f"通过元类type的__call__方法创建的实例对象Three类: {Three}  由 {Three.__class__} 创建\n")

# 通过One元类创建类，实例化对象Four
# 实际是使用One的__call__方法
# __call__方法调用__new__方法，返回Four类
# __call__方法调用__init__方法，初始化Four类
Four = One("Four", (object,), {})
print(f"通过元类One的__call__方法创建的实例对象Four类: {Four}  由 {Four.__class__} 创建\n")
