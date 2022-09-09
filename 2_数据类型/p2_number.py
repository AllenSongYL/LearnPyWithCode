# -*- coding: utf-8 -*-
# @time:         2022/8/27 17:28
# @Author:       Alan
# @File:         p2_number.py
# @Software:     PyCharm
# @Description:  基本数据类型 -  数字

import math
# todo 1.0 数字类型
"""
存储数字的数据类型。
三种不同的数值类型
- 整数    正或负整数，不带小数点
- 浮点数   浮点型由整数部分与小数部分组成
- 复数     复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示

特性
- 不可变，改变值重新分配内存

数字运算符
+          加
-          减
*          乘
/          浮点除
//         整除
%          模(余数)
**         幂运算
"""

aInt = 100
print(f"这是一个整数(int)类型: {aInt}, 类型: {type(aInt)}, 地址: {id(aInt)}")
aInt = aInt + 100
print(f"改变后的值: {aInt}, id: {id(aInt)}")
print("===数字不可变类型，改变数字类型的值，将重新分配内存===", end="\n\n")

bFloat = 3.1415
print(f"这是一个浮点(float)类型: {bFloat}, 类型: {type(bFloat)}")

cComplex = complex(2, 4)
print(f"这是一个复数(complex)类型: {cComplex}, 类型: {type(cComplex)}")
cComplex2 = 2 + 3j
print(cComplex2)
print("===数字类型类别===", end="\n\n")

# todo 1.1  数字类型转换
print(f"整数 {aInt} 转浮点数: {float(aInt)}")
print(f"整数 {aInt} 转复数: {complex(aInt)}")
print(f"浮点数 {bFloat} 转整数: {int(bFloat)}")
print(f"浮点数 {bFloat} 转复数: {complex(bFloat)}")
# 复数不能转换为整数和浮点数
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
# print(f"复数 {cComplex} 转整数: {int(cComplex)}")
# print(f"复数 {cComplex} 转整数: {float(cComplex)}")
print("===数字类型转换===", end="\n\n")

# todo 1.2 数字运算
print(f"2.1 + 2 = {2.1 + 2}")
print(f"50 - 2 * 2 = {50 - 2*2}")
# / 除法总是返回一个浮点数
print(f"25 / 5 = {25 / 5}")
# // 整除，丢弃小数点部分
print(f"25 // 5 = {25 // 5 }")
print(f"25 // 2 = {25 // 2 }")
print(f"9 % 3 = {9 % 3}")
print(f"5 % 2 = {5 % 2}")
print(f"2 ** 3 = {2 ** 3}")
print("===数字运算===", end="\n\n")

# todo 1.3 数学函数

# todo 1.3.1 abs(num)
# 返回绝对值
print(f"abs(-10) = {abs(-10)}")

# todo 1.3.2 ceil(num)
# 返回向上取整的整数
print(f"ceil(10.5) = {math.ceil(10.5)}")
print(f"ceil(10.1) = {math.ceil(10.1)}")
print(f"10.5.__ceil__() = {10.5.__ceil__()}")
print("===math.ceil===", end="\n\n")

# todo 1.3.3 floor(num)
# 返回向下取整的整数
print(f"math.floor(2.1) = {math.floor(2.1)}")
print(f"math.floor(2.7) = {math.floor(2.7)}")
print("===math.floor===", end="\n\n")

# todo 1.3.4 log(num)
# 返回自然数，返回值 > 0
print(f"math.log(100.12) = {math.log(100.12)}")
print(f"math.log(100) = {math.log(100)}")
print(f"math.log(math.pi) = {math.log(math.pi)}")
print("===log===", end="\n\n")

# todo 1.3.5 max(num1, num2, ...)
# 返回最大值
print(f"max(1, 3, 5, 66, 99, 24) = {max(1, 3, 5, 66, 99, 24)}")
print("===max===", end="\n\n")

# todo 1.3.6 min(num1, num2, ...)
# 返回最小值
print(f"min(1, 3, 5, 66, 99, 24) = {min(1, 3, 5, 66, 99, 24)}")
print("===min===", end="\n\n")

# todo 1.3.7 modf(num)
# 返回num的小数点部分和整数部分, 返回类型为tuple元组
print(f"math.modf(100.12) = {math.modf(100.12)}")
print(f"math.modf(-100.12) = {math.modf(-100.12)}")
print(f"math.modf(-100.12) = {type(math.modf(-100.12))}")
print("===math.modf===", end="\n\n")

# todo 1.3.8 pow(x, y, [z])
# 等效于: x ** y % z
print(f"pow(2,3) = {pow(2,3)}")
print(f"pow(2,3,2) = {pow(2,3,2)}")
print("===pow===", end="\n\n")

# todo 1.3.9 round()
# 当个位数为偶数时，小数部分>5， 向上取整，否则向下取整
# 当个位数为奇数时，小数部分>=5，向上取整，否则向下取整
# 4舍6入5看齐,奇进偶不进
print(f"round(2.4) = {round(2.4)}")
print(f"round(2.5) = {round(2.5)}")
print(f"round(2.6) = {round(2.6)}")
print(f"round(3.4) = {round(3.4)}")
print(f"round(3.5) = {round(3.5)}")
print("===round===", end="\n\n")
