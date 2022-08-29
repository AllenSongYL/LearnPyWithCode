# -*- coding: utf-8 -*-
# @time:         2022/8/29 12:49
# @Author:       Alan
# @File:         p1_for.py
# @Software:     PyCharm
# @Description:  for循环

# todo 1.0 for循环
"""
for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。

格式
for 变量 in 序列:
    代码块
else:
    代码块

else 循环结束后执行，不推荐使用else

"""
for i in [1, 2, 3, 4, 5]:
    print(f"循环中, i的值{i}")
else:
    print("else代码块")
print("===for列表===", end="\n\n")

# todo 1.1 range([0],stop)
# 生产指定数列，不包含结尾的stop
for i in range(10):
    print(f"使用range P1, i的值{i}")
for i in range(2, 6):
    print(f"使用range P2, i的值{i}")
print("===for range===", end="\n\n")

# todo 1.2 break
# 跳出循环，停止本层后面的循环;
# 不会停止上一级循环体
for i in range(10):
    if i == 5:
        break
    else:
        print(f"使用range P3, i的值{i}")

for j in range(10):
    print(f"- {j}")
    for i in range(10):
        if i == 5:
            break
        else:
            print(f"使用range P4, i的值{i}")
print("===break===", end="\n\n")

# todo 1.3 continue
# 跳过本次循环，继续后面的循环
for i in range(10):
    if i == 5:
        continue
    else:
        print(f"使用range P5, i的值{i}")
print("===continue===", end="\n\n")