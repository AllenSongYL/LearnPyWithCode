# -*- coding: utf-8 -*-
# @time:         2022/8/28 16:21
# @Author:       Alan
# @File:         p2_operator.py
# @Software:     PyCharm
# @Description:  operator模块

import operator

a = [1, 2]
b = [1, 2]
c = [2, 3]

print(id(a), id(b))
print(f"{a} 等于 {b} : {operator.eq(a, b)}")
print(f"{a} 等于 {c} : {operator.eq(a, c)}")
print(f"{a} 小于 {c} : {operator.lt(a, c)}")

