# -*- coding: utf-8 -*-
# @time:         2022/8/30 16:13
# @Author:       Alan
# @File:         p4_enum.py
# @Software:     PyCharm
# @Description:
from enum import Enum, unique


# @unique装饰器帮我们检查保证没有重复值
@unique
class Weekday(Enum):
    # 类属性；静态属性
    Sum = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
