# -*- coding: utf-8 -*-
# @time:         2022/8/27 21:19
# @Author:       Alan
# @File:         P1_random.py
# @Software:     PyCharm
# @Description:  random模块 生成伪随机数

# 导入random模块
import random

# todo 1.0 random 生产随机数
""" 
在半开放区间 [0.0,1.0) 内均匀生成随机浮点数

"""

# todo 1.1 初始化随机数生成器
# 不指定默认使用系统时间
random.seed()

# 返回生成器当前内部状态的对象(元组)
print(random.getstate())
print(type(random.getstate()))

#  todo 1.2 random()
#  返回 0.0 <= x < 1.0 的浮点数
print(f"random() = {random.random()}")

# todo 1.3 uniform(float1, float2)
# 返回给定参数范围区间的随机浮点数
print(random.uniform(3.5, 10.6))
print(random.uniform(10.6, 3.5))

# todo 1.4 randrange([start], stop, [step])
# 返回指定范围的随机整数 不包含结束位置
# start 起始位置(整数)
# stop  结束位置(整数)
# step  步长值(整数)
# 相当于choice(range(start, stop, step))
print(f"random.randrange(3) = {random.randrange(3)}")
# ValueError: non-integer arg 1 for randrange()
# print(f"random.randrange(10.5) = {random.randrange(10.5)}")
print(f"random.randrange(10,100) = {random.randrange(10, 100)}")
print(f"random.randrange(10,100,2) = {random.randrange(10, 100, 2)}")
print(f"random.randrange(0,4,2) = {random.randrange(0, 4, 2)}")

# todo 1.5 randint(int1, int2)
# int1 <= 返回值 <= int2
print(f"random.randint(3, 8) = {random.randint(3, 8)}")

# todo 1.6 choice(seq)
# 从非空序列中返回一个随机元素
print(f"random.choice([5,25,55,8]) = {random.choice([5, 25, 55, 8])}")
# IndexError: list index out of range
# print(f"random.choice([]) = {random.choice([])}")

# todo 1.7 shuffle(gather)
# 接受一个序列，并以随机顺序改变序列，返回None
alist = [5, 6, 7, 8, 9]
print(f"shuffle前: {alist}")
print(f"random.shuffle(alist) = {random.shuffle(alist)},")
print(f"shuffle后: {alist}")

# todo 1.8 sample(gather, k)
# 从gather随机抽取指定长度的元素
# k  返回长度
print(f"{random.sample(alist, k=2)}")
print(f"{random.sample([4,4,5,1], k=2)}")
