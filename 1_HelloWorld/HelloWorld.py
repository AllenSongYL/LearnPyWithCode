# -*- coding: utf-8 -*-
# @time:        2022/8/26 9:56
# @Author:      Alan
# @File:        1_HelloWorld.py
# @Software:    PyCharm
# @Description: First run

import keyword

# todo 0. print输出到控制台
"""
- 将值打印到流中，默认情况下打印到 sys.stdout。且默认换行。
- sep: print多个时，指定分隔符
- end: 在最后一个值之后附加的字符串，默认为换行符。可以使用end=""，取消换行
- file: 类文件对象。默认是sys.stdout
"""


print("Hello World !")
print("Hello World2!", end="")
print("H", "e", "l", "l", "w", "o", "r", "l", "d", "3", sep="|")
with open("output.txt", "a+") as f:
    print("Print output to file!", file=f)
print("===print===")

# todo 1. 注释
# 这是单行注释 print不会执行，解析器忽略该行代码
# print("Hello World!")

# 这是多行注释
"""
    print("Hello World!")
"""
print("===注释===")

# todo 2. 标识符
"""
- 命名规则
    - 对各种 变量、方法、函数等命名时使用的字符序列称为标识符。
    - 标识符由26个英文字母大小写，0-9，_组成
    - 不能以数字开头
    - 严格区分大小写
    - 不能包含空格、@、%等特殊字符
    - 不能以系统保留关键字作为标识符
- 命名规范
    - 尽量采用有意义的名称
    - 模块名时（单个py文件）：          尽量短小，全部使用小写字母，可以使用下划线分隔多个字母
    - 包名时（包含多个py文件的文件夹）：  尽量短小，全部使用小写字母，推荐使用-
    - 类名时：                        单词首字母大写
- 特殊含义
    - _标识符                             表示不能直接访问，内部属性
    - __标识符                            私有成员
    - __init__                          专用标识符    
"""
# 定义字符串
aString = "张三"
print(aString)
# 定义整数类型
bInt = 10
print(bInt)
# 定义浮点类型
cFloat = 10.232
print(cFloat)
print("===标识符===")

# todo 3. Python关键字
"""
保留字及关键字，不能作为标志符。标准库提供了keyword模块，可以输出当前版本所有关键
"""
buildinKW = keyword.kwlist
print("当前版本所有关键字: ", buildinKW)
print("关键字数量: ", len(buildinKW))
print("===关键字===")

# todo 4. 缩进和换行
"""
Python特色：
使用缩进来表示代码块，不需要使用{}
缩进4个空格，同一级代码块使用相同的缩进空格数
使用"\" 来实现多行语句
"""
if True:
    print("这一行太长了\
    换行输入")
print("===缩进和换行===")

