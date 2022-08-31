# -*- coding: utf-8 -*-
# @time:         2022/8/29 10:37
# @Author:       Alan
# @File:         p7_set&frozeset.py
# @Software:     PyCharm
# @Description:  set集合

# todo 1.0 集合介绍
"""
set集合
集合是0~n个对象引用的无序集合，集合中存储的元素不可重复，因此这些对象引用的引用的对象必须是可哈希运算的 。

格式: {value1, value2, value3 }
- 特点
    - 可变
    - 无序, 没有索引,不能使用分片操作符进行操作。
    - 元素不能重复
    - 存放可哈希的类型，如str字符串、数字、tunple元组。(可变类型为不可哈希，如: dict字典，list列表，set集合)


frozeset
和set集合类似，但是创建后不能改变
"""

# todo 1.1 创建set集合
set1 = {1, 2}
# set1 = {1, 2, 3, 4, 1}
print(f"值：{set1}, 类型: {type(set1)}")
# 创建空集合,不能直接使用{}，这是空字典的形式
set2 = {}
print(type(set2))
set3 = set()
print(type(set3))

# TypeError: unhashable type: 'list'
# TypeError: unhashable type: 'set'
# TypeError: unhashable type: 'dict'
# set4 = {1, "a", True, None, [1, 2, 3], 11.22}
# set4 = {1, "a", True, None, {1, 23, 4}, 11.22}
set4 = {1, "a", True, None, (1, 23, 4), 11.22}
print(set4)
print("===创建集合===", end="\n\n")

# todo 1.2 set操作集合
# todo 1.2.1 add(x)
# 添加单个元素
set1.add("a")
print(set1)
# TypeError: set.add() takes exactly one argument (2 given)
# set1.add("b", "c")
# 添加已存在的元素，不进行任何操作
set1.add(1)
# 可以添加一个集合类型
set1.add((1, 2, 3))
print(set1)
print("===add添加===", end="\n\n")

# todo 1.2.2 update(x)
# 将x中每个元素，单独添加到集合
set1.update({21, 22})
print(f"添加集合: {set1}")
set1.update((7, 8))
print(f"添加元组: {set1}")
set1.update([17, 18])
print(f"添加列表: {set1}")
set1.update("字符串串")
print(f"添加字符串: {set1}")
set1.update({"新新旧旧值"})
print(f"添加字符串集合: {set1}")
print("===update添加===", end="\n\n")

# todo 1.2.3 remove()
# 删除集合中指定的值; 删除不存在的值会报错: KeyError: 'ppap'
set1.remove("新新旧旧值")
print(set1)
# set1.remove("ppap")
print("===remove删除===", end="\n\n")

# todo 1.2.4 discard()
# 删除集合中指定的值; 删除不存在的值不会报错
set1.discard("字")
print(set1)
set1.discard("字")
print("===discard删除===", end="\n\n")

# todo 1.2.5 pop()
# 随机删除集合中的元素;返回被删除的元素
print(set1.pop())
print(set1)
print("===pop删除===", end="\n\n")

# todo 1.2.6 len(set)
# 计算集合中元素数量
print(len(set1))
print("===len()===", end="\n\n")

# todo 1.2.7 clear()
# 清空集合；返回None
set4 = {7, 8, 9, 0}
print(set4)
print(set4.clear())
print(set4)
print("===clear()===", end="\n\n")

# todo 1.2.8 in
# 判断元素是否在集合中
if "串" in set1:
    print("YES!IN")
print("===in===", end="\n\n")

# todo 1.2.9 copy()
# 浅拷贝
set5 = set1.copy()
print(f"原id: {id(set1)}, 拷贝: {id(set5)}\n值: {set5}")
set5.remove('a')
print(f"原集合: {set1}\n新集合: {set5}")
print("===copy()===", end="\n\n")

aset = {1, 2, 3}
bset = {0, 2, 4}

# todo 1.2.10 difference()
# 和 - 差集一致;返回aset有而bset没有的元素
print(aset.difference(bset))
print("===difference()===", end="\n\n")

# todo 1.2.11 difference_update(x)
# 删除aset中在bset中已存在的元素
print(aset.difference_update(bset))
print(aset)
print(bset)
print("===difference_update()===", end="\n\n")

aset.add(2)
# todo 1.2.12 intersection()
# 返回两个集合的交集 和&效果一致
print(aset.intersection(bset))
print("===intersection()===", end="\n\n")

# todo 1.2.13 isdisjoint(set)
# 两个集合没有相同元素则返回True，否则返回False
print(aset, bset)
print(aset.isdisjoint(bset))
print("===intersection()===", end="\n\n")

# todo 1.2.14 issubset()
# 判断aset元素是否均在bset中，是则True，否则False
print(aset.issubset(bset))
print(aset.issubset((1, 2, 3, 4, 5, 6)))
print("===issubset()===", end="\n\n")

# todo 1.2.15 issuperset()
# 判断集合aset是否包含bset集合中所有元素，是则True，否则False
print(aset.issuperset(bset))
print(aset.issuperset((1,)))
print("===issuperset()===", end="\n\n")

# todo 1.3 集合运算
# todo 1.3.1 & 交集
# 取两个集合公共的元素
print(f"交集: {aset & bset}")

# todo 1.3.2 | 并集
# 去重，取出两个集合全部元素
# union()
print(f"并集: {aset | bset}")

# todo 1.3.3 - 差集
# 取前一个集合有，后集合没有的元素
print(f"差集: {aset - bset}")

# todo 1.3.4 ^ 对称差集
# 对 &交集取反 和symmetric_difference()方法一致
print(f"交集取反: {aset ^ bset}")

# todo 1.4 frozenset
# 创建之后不能改变的集合
fs = frozenset()
print(f"fs = {fs}, type(fs) = {type(fs)}")

fs1 = frozenset("frozenset")
print(f"fs1 = {fs1}, type(fs1) = {type(fs1)}")

fs2 = frozenset(range(10))
print(f"fs2 = {fs2}, type(fs2) = {type(fs2)}")

# 没有update, remove. discard, pop, clear等改变集合的方法
