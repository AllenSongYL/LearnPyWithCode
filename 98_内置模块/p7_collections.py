# -*- coding: utf-8 -*-
# @time:         2022/9/1 16:15
# @Author:       Alan
# @File:         p7_collections.py
# @Software:     PyCharm
# @Description:  collections 模块


"""
https://docs.python.org/zh-cn/3/library/collections.html#collections.Counter

collections 模块
容器数据类型
这个模块实现了特定目标的容器，以提供Python标准内建容器 dict , list , set , 和 tuple 的替代选择
Counter     字典的子类，提供了可哈希对象的计数功能
namedtuple() 工厂函数用来创建一个带字段名的元组和一个有名字的类来对它进行引用
deque       双端队列; 类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop)
ChainMap    字典的集合类; 用于链接多个映射(mapping)对象，形成一个单一的可更新的视图
OrderedDict 字典的子类，保留了他们被添加的顺序
defaultdict 字典的子类，提供了一个工厂函数来初始化每个键所对应的值
UserDict    包装标准的 dict 对象，以便于扩展
UserList    包装标准的 list 对象，以便于扩展
UserString  包装标准的 string 对象，以便于扩展
"""

import collections

# todo 1.0 Counter
"""
Counter 是一个 dict 的子类，用于计数可哈希对象
Counter 对象是一个无序的容器类型，以字典的键值对形式存储，其中元素作为 key，其计数作为 value
计数值可以是任意的 Interger 值，包括 0 和负数
Counter 对象可以被用在任何需要制表或者计数的场合
Counter 对象和其他语言的 bags 或者 multiset 类似
"""

# todo 1.0.1 创建Counter
# Counter 对象的创建
# 从一个可迭代对象创建
a = collections.Counter('abracadabra')
print(a, type(a), a['a'])
print(collections.Counter())
print(collections.Counter({'red': 4, 'blue': 2}))
print(collections.Counter(cats=4, dogs=8))
print("===创建Counter对象===", end="\n\n")

# todo 1.0.2 elements
# elements() 方法返回一个迭代器，可以产生所有元素的重复出现次数的序列
print(a.elements(), type(a.elements()))
for i in a.elements():
    print(i, end=' ')
print("===elements===", end="\n\n")

# todo 1.0.3 most_common
# most_common() 方法返回一个列表，其中包含出现次数最多的元素和它们的计数，从最多到最少排序
# 如果 n 没有被指定，则返回所有元素 如果 n 被指定，则返回计数最多的 n 个元素
print(a.most_common(2))
print(a.most_common(3))
print(a.most_common())
print("===most_common===", end="\n\n")


# todo 1.0.4 update
# update() 方法用来更新计数器
# 可以是一个可迭代对象，也可以是一个映射对象
# 从 迭代对象 计数元素或者 从另一个 映射对象 (或计数器) 添加。
# 像 dict.update() 但是是加上，而不是替换。
# 另外，迭代对象 应该是序列元素，而不是一个 (key, value) 对。
print(a)
a.update('aaaaazzz')
print(a)
print("===update===", end="\n\n")

# todo 1.0.5 subtract
# subtract() 方法用来减少计数器中的元素
# 可以是一个可迭代对象，也可以是一个映射对象
# 从 迭代对象 计数元素或者 从另一个 映射对象 (或计数器) 减少。
# 像 dict.update() 但是是减去，而不是替换。
# 另外，迭代对象 应该是序列元素，而不是一个 (key, value) 对。
print(a)
a.subtract('aaabzzcc')
print(a)
print("===subtract===", end="\n\n")

# todo 1.0.6 total
# total() 方法返回计数器中所有元素的总计数
print(a)
print(a.total())
print("===total===", end="\n\n")

# todo 1.0.7 Counter运算符
# Counter 对象支持 + 和 - 运算符
# 运算符 + 用于合并计数
# 运算符 - 用于减少计数
# 运算符 & 和 | 用于计数的交集和并集
# 运算符 + 和 - 会移除结果中的零和负计数
# 运算符 & 和 | 不会移除结果中的零和负计数
# 运算符 + 和 - 会将所有输入转换为 Counter 对象
# 运算符 & 和 | 只会转换 Counter 对象和整数或者可转换为整数的映射对象
c = collections.Counter(a=3, b=1)
d = collections.Counter(a=1, b=2)
# + 运算符 合并计数
print(f"c: {c}\nd: {d}")
print(f"c + d:\n{c + d}")
print("=== + 相当于 c[x] + d[x]===", end="\n\n")

# - 运算符 用于减少计数 会移除结果中的零和负计数
# 和subtract()方法不同的是，运算符 - 会移除结果中的零和负计数, 而subtract()方法不会移除结果中的零和负计数
# subtract()改变原来的计数器，而运算符 - 不会改变原来的计数器
print(f"c: {c}\nd: {d}")
print(f"c - d:\n{c - d}")
print("=== - 相当于 subtract只保留正数 ===", end="\n\n")

print(f"c: {c}\nd: {d}")
print(f"c & d:\n{c & d}")
print("=== & 相当于 min(c[x], d[x]) ===", end="\n\n")

print(f"c: {c}\nd: {d}")
print(f"c | d:\n{c | d}")
print("=== | 相当于 max(c[x], d[x]) ===", end="\n\n")