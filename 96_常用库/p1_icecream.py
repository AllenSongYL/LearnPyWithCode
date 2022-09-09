# -*- coding: utf-8 -*-
# @time:         2022/8/31 14:55
# @Author:       Alan
# @File:         p1_icecream.py
# @Software:     PyCharm
# @Description:  icecream

from icecream import ic
import time

# 打开输出
ic.enable()
# 关闭输出
# ic.disable()

# todo 1.0 自定义输出格式
# prefix 指定前缀
ic.configureOutput(prefix="[alan] ---> ")


def timeformat():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " alan --> "


# includeContext 是否包含上下文
# 默认False
ic.configureOutput(prefix=timeformat, includeContext=True)

a = [1, 2, 3, 4, 5]
ic(a, type(a))
ic("hello")
