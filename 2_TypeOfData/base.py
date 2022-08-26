# -*- coding: utf-8 -*-
# @time:         2022/8/26 11:11
# @Author:       Alan
# @File:         base.py
# @Software:     PyCharm
# @Description:  数据类型

# todo 1. 字符串类型
"""
最常用的数据类型。可以使用双引号或单引号创建字符串

特性
- 不可变

操作运算符
+          字符串拼接
*          重复输出
[]         通过索引获取获取字符串
"""

# 定义字符串
aString = "张三"
print(aString)
print(type(aString))
# 值传递，bString改变不会影响aString
bString = aString
bString = bString + "和李四"
print(aString)
print(bString)

# 拼接字符串
print("abcd" + "ABCD")

# 重复输出
cString = "A"
dString = cString * 10
print(dString)

# 使用索引
# 起始索引从0开始,从左往右0,1,2;从右往左-1,-2,-3
# 左闭右开 结尾索引为6，[:6]时不输出最后字符
# 起始索引0，结束索引-1 可以省略
eString = "0123456"
print("eString[4] : ", eString[4])
print("eString[2:4] : ", eString[2:4])
print("eString[:4] :", eString[:4])
print("eString[3:] :", eString[3:])
print("eString[:6] :", eString[:6])
print("eString[-3:-1] :", eString[-3:-1])
print("eString[-3:0] : ", eString[-3:])

# in 运算符 返回True或False
print("in 成员运算符，返回结果： ", "2" in eString)
