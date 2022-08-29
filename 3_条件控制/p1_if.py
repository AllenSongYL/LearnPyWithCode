# -*- coding: utf-8 -*-
# @time:         2022/8/29 12:10
# @Author:       Alan
# @File:         p1_if.py
# @Software:     PyCharm
# @Description:  条件控制语句


# todo 1.0 if 条件控制
"""
通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块

if 语句格式
if 条件表达式1:
    执行语句1
elif 条件表达式2:
    执行语句2
else:
    执行语句3

执行顺序
    - 如果 "条件表达式1" 返回的结果是True，则执行 "执行语句1"; 返回结果是"False"
    - 判断 " 条件表达式2" 返回的结果，True，则执行 "执行语句2"; 如果结果是"False"
    - 执行最终else下的 "执行语句3"

注意：
1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3. if 条件表达式返回值为布尔值

"""

# todo 1.1 if 语句
score = 78
if 0 <= score < 60:
    print("不及格")
elif score < 80:
    print("良好")
else:
    print("优秀")

# todo 1.2 判断运算符
# todo 1.2.1 < 小于      返回布尔值(True/False)
print(f"10 < 10 = {10 < 10}")
print(f"10 < 20 = {10 < 20}")

# todo 1.2.2 <= 小于等于 返回布尔值(True/False)
print(f"10 <= 20 = {10 <= 20}")
print(f"10 <= 10 = {10 <= 10}")
print(f"20 <= 10 = {20 <= 10}")

# todo 1.2.3 > 大于      返回布尔值(True/False)
print(f"20 > 10 = {20 > 10}")

# todo 1.2.4 >= 大于等于 返回布尔值(True/False)
print(f"20 >= 10 = {20 >= 10}")

# todo 1.2.5 == 等于     返回布尔值(True/False)
print(f"20 == 10 = {20 == 10}")
print(f"20 == 20 = {20 == 20}")

# todo 1.2.6 != 不等于    返回布尔值(True/False)
print(f"20 != 10 = {20 != 10}")
print(f"20 != 20 = {20 != 20}")

# todo 1.2.7 in
if 1 in [1,2]:
    print("YES! in")

# todo 1.2.8 空值
# 0,[],None,'',() 均为False;
if []:
    print("True")
else:
    print("False")

if 0:
    print("True")
else:
    print("False")

if None:
    print("True")
else:
    print("False")

if ():
    print("True")
else:
    print("False")

if '':
    print("True")
else:
    print("False")

if {}:
    print("True")
else:
    print("False")