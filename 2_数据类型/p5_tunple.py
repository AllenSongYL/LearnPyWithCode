# -*- coding: utf-8 -*-
# @time:         2022/8/28 15:52
# @Author:       Alan
# @File:         p5_tunple.py
# @Software:     PyCharm
# @Description:  元组

# todo 1.0 tunple元组
"""
序列中每个值都有相对应的位置值，称为索引。
使用"()"创建，元素之间用逗号分隔
- 特点
    - 有序
    - 不可变 （是元组所指向的内存中的内容不可变）
    - 允许重复成员
    - 可包含任意数据类型
- 索引
    - 从左往右，从0开始，左闭右开
    - 从右往左，从-1开始，-2，-3，-4以此类推
    - [位置索引] 取单个元素
    - [起始位置:结束位置:步长值]
- 运算符
    - "+"    元组拼接
    - "*"    元组复制
    - "in"   元素是否存在
"""

# todo 1.1 创建列表
aTunple = ("a", "b", 1, 2, 4.3, True, ["cef", "pas"])
print(aTunple, type(aTunple))
bTunple = "z", "x", 1
print(bTunple, type(bTunple))
# 仅包含单个元素时，需要在元素后面加逗号，否则会把()当成运算符
cTunple = ("one",)
print(cTunple, type(cTunple))
dTunple = ("one")
print(dTunple, type(dTunple))
print("===创建列表===", end="\n\n")

# todo 1.2 使用索引
print(f"aTunple[4] = {aTunple[4]}")
print(f"aTunple[1:4] = {aTunple[1:4]}")
print(f"aTunple[-4:-1] = {aTunple[-4:-1]}")
print(f"aTunple[6][0] = {aTunple[6][0]}")
print(f"aTunple[::2] = {aTunple[::2]}")
print("===通过索引index获取值===", end="\n\n")

# todo 1.3 不能修改元组
# 但是可以修改元组中，引用的可变数据类型,如列表
# TypeError: 'tuple' object does not support item assignment
# aTunple[0] = "aaa"
aTunple[6][0] = "new_cef"
aTunple[6][1] = "new_pas"
print(aTunple)
print("===不可变===", end="\n\n")

# todo 1.4 删除元组

# 不能删除单个元素
# TypeError: 'tuple' object doesn't support item deletion
# del aTunple[0]
print(f"删除前: {dTunple}")
del dTunple
# 名称 'dTunple' 可能未定义
# print(f"删除后: {dTunple}")
print("===删除元组===", end="\n\n")

# todo 1.5 元组运算符
# todo 1.5.1 + 拼接运算符
# 合并元组生产新的元组，需要有变量接收
etunlp = cTunple + (4, "a","g")
print(f"使用+运算符: {etunlp}")

# todo 1.5.2 * 重复运算符
fTunple = etunlp * 3
print(f"使用*运算符: {fTunple}")

# todo 1.5.3 in 判断是否存在元素
print(f"in 判断元素是否在元组中：{3 in fTunple}")
print(f"in 判断元素是否在元组中：{'a' in fTunple}")


# todo 1.6 遍历元组
for i in fTunple:
    print(i)
print("===遍历元组===", end="\n\n")

# todo 内置函数
# todo len() 计算元素个数
print(f"fTunple个数: {len(fTunple)}")

#

# todo 1.7 元组推导式(生成器表达式)
# 对序列或可迭代对象中的每个元素应用某种操作，用生成的结果创建新的列表；或用满足特定条件的元素创建子序列
# 格式： (表达式 for 变量 in 列表 [if 条件])
# 返回： 生成器对象
xTunple = (i for i in range(10) if i % 2 == 0)
print(f"[i for i in range(10) if i % 2 == 0] = {xTunple}")
print(xTunple.__next__())
print(xTunple.__next__())
print(xTunple.__next__())