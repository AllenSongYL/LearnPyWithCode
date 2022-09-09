# -*- coding: utf-8 -*-
# @time:         2022/9/8 11:32
# @Author:       Alan
# @File:         p2_类内置属性和方法.py
# @Software:     PyCharm
# @Description:


class Per:
    """
    ====================
    |    测试类         |
    ====================
    """

    pass

# 类的属性（包含一个字典，由类的数据属性组成）
print(f"Per类属性: {Per.__dict__}")
# 类的父类，所有父类组成的元组
print(f"Per类的父类: {Per.__bases__}")
# 类的注释
print(f"Per类的文档: {Per.__doc__}")
# 类的名称
print(f"Per类的名称: {Per.__name__}")
# 类定义所在模块
print(f"Per类的名称: {Per.__module__}")

p = Per()
#
print(f"p对象的类: {p.__class__}")
