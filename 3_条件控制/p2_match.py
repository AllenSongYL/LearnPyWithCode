# -*- coding: utf-8 -*-
# @time:         2022/8/29 12:38
# @Author:       Alan
# @File:         p2_match.py
# @Software:     PyCharm
# @Description:  条件控制语句

# todo 1.0 match-case 条件控制
"""
python 3.10 新特性
match-case 结构模式匹配
match 语句接受一个表达式并将其值与作为一个或多个 case 块给出的连续模式进行比较


顺序依次匹配

match语句格式：
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>

"""

#
score = 0
match score:
    case 0:
        print("girl")
    case 1:
        print("boy")
    case 2 | 3 | 4:
        print("unknow")
