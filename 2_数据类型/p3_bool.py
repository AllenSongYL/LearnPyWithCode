# -*- coding: utf-8 -*-
# @time:         2022/8/27 21:31
# @Author:       Alan
# @File:         p3_bool.py
# @Software:     PyCharm
# @Description:  bool 布尔类型

# todo 1.0 布尔类型
"""
只有两个值
- True
- False
"""

print(f"1 > 10 = {1 > 10}")
print(f"10 > 1 = {10 > 1}")
# todo 1.1 bool()
# 评估函数，如果评估的值为空，数字0，和None，返回False；否则返回True。
print(bool("a"))
print(bool(""))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(None))
print(bool(()))
print("===bool()===", end="\n\n")

# 常用于if else语句
if 2 > 1:
    print("yes")
else:
    print("no")

