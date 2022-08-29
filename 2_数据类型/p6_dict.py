# -*- coding: utf-8 -*-
# @time:         2022/8/29 9:00
# @Author:       Alan
# @File:         p6_dict.py
# @Software:     PyCharm
# @Description:  使用dict字典数据类型

# todo 1.0 dict 字典
"""
键值对 的集合
字典以 关键字 为索引，关键字通常是字符串或数字，也可以是其他任意不可变类型。
格式: {key1 : value1, key2 : value2, key3 : value3 }
- 特点
    - 可变
    - key键必须是唯一的，值可以重复
    - 可包含任意数据类型
    - 有序 按插入次序排序
"""


# todo 1.0 创建字典
dict1 = {'a': 1, 'b': 2, 'c': 3, "d": [1, 2, 3, 4]}
print(f"dict1值: {dict1}, 类型: {type(dict1)}")
dict2 = {}
print(f"dict2值: {dict2}, 类型: {type(dict2)}")
# 使用dict()构造函数创建字典
dict3 = dict(f=1, d=2, g=3)
print(dict3)
dict4 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict4)
print("===创建字典===", end="\n\n")

# todo 1.2 访问字典中的值
print(dict1["a"])
# 键不存在会报错: KeyError: 'f'
# print(dict1["f"])
print("===访问字典===", end="\n\n")

# todo 1.3 修改字典中的值
dict1['a'] = "xyz"
print(f"dict1['a'] = 'xyz'\"' = {dict1}")
print("===字典修改===", end="\n\n")

# todo 1.4 字典添加
dict1['new'] = 999
print(dict1)
print("===字典添加===", end="\n\n")

# todo 1.5 删除字典中的元素
del dict1['new']
print(dict1)
print("===字典删除元素===", end="\n\n")

# todo 1.6 字典内置方法
# todo 1.6.1 copy 浅拷贝
print(dict1)
dict5 = dict1.copy()
print(f"dict1内存地址: {id(dict1)}, dict5内存地址: {id(dict5)}")
dict5['a'] = 'abc'
print(f"修改不会影响原字典\ndict1: {dict1}\ndict5: {dict5}")
dict5["d"].append("ap")
print(f"修改字典中的引用类型数据，会影响原字典 \ndict1: {dict1}\ndict5: {dict5}")
print("===copy()浅拷贝===", end="\n\n")

# todo 1.6.2 fromkeys(seq, [default=None])
# 将序列中的元素作为字典的key, 默认为None可以指定默认vlaue
# seq     指定序列
# default 字典默认的值
dict6 = dict.fromkeys(["ee", "ff", "gg"], 1)
print(dict6)
dict6 = dict.fromkeys(["ee", "ff", "gg"])
print(dict6)
print("===fromkeys方法===", end="\n\n")

# todo 1.6.3 get(key, [default=None])
# 返回指定key的值，如果不存在返回默认值
# 对比 字典[key] 如果key不存在会报错
print(dict1.get("a"))
print(dict1.get("jj", "无"))
print("===get方法===", end="\n\n")

# todo 1.6.4 keys()
# 获取字典中所有的key，返回一个视图对象 <class 'dict_keys'>
# 该对象提供字典条目的一个动态视图，这意味着当字典改变时，视图也会相应改变。
# 字典视图可以被迭代以产生与其对应的数据，并支持成员检测
d1_keys = dict1.keys()
print(f"key()结果: {d1_keys}, 类型: {type(d1_keys)}")
# 返回的对象不能使用索引, 可以使用list转换为列表
# print(d1_keys[0])
d1_keys = list(d1_keys)
print(type(d1_keys))
print("===keys方法===", end="\n\n")

# todo 1.6.5 items()
# 返回一个视图对象 <class 'dict_items'> 可以遍历key/value键值对
# 该对象提供字典条目的一个动态视图，这意味着当字典改变时，视图也会相应改变。
# 该对象不是列表，不支持索引，可以使用list转换为列表
d1_items = dict1.items()
print(f"值{d1_items}, 类型 {type(d1_items)}")
print("===items方法===", end="\n\n")

# todo 1.6.6 values()
# 返回一个视图对象 <class 'dict_values'> 包含字典中所有的值
# 该对象提供字典条目的一个动态视图，这意味着当字典改变时，视图也会相应改变。
# 该对象不是列表，不支持索引，可以使用list转换为列表
d1_values = dict1.values()
print(f"值{d1_values}, 类型 {type(d1_values)}")
print("===values方法===", end="\n\n")

# todo 1.6.7 setfefault(key, [default=None])
# 添加键，默认为None，可以指定值
dict1.setdefault("ping", "pong")
print(dict1)
dict1.setdefault("jojo")
print(dict1)
print("===setfefault方法===", end="\n\n")

# todo 1.6.8 update(dict2)
# 合并字典 返回None；对原字典进行添加
print(dict1.update({1: "a", 2: "b"}))
print(dict1)
print("===update方法===", end="\n\n")

# todo 1.6.9 |= 运算符
# 合并运算符
dict1 |= {3: "c", 4: "d"}
print(dict1)
print("==='|='运算符===", end="\n\n")

# todo 1.6.10 pop(key, [default])
# 删除字典key对应的值，返回被删除的值
# default 当key不存在返回的值;如果key不存在且未指定default则报KeyError
print(dict1.pop(4))
print(dict1)
print(dict1.pop("jj", "no"))
# KeyError: 'jj'
# print(dict1.pop("jj"))
print("===pop方法===", end="\n\n")

# todo 1.6.11 popitem()
# 删除最后一组key，value，并返回元组
print(dict1)
print(dict1.popitem())
rmdictv = dict1.popitem()
print(type(rmdictv))
print(dict1)
print("===popitem方法===", end="\n\n")

# todo 1.6.12 清空字典
print(dict3)
dict2.clear()
print(f"clear清空字典: {dict3}")
print("===清空字典中所有元素===", end="\n\n")

# todo 1.6.13 len()
# 计算字典元素个数，即key的总数
print(len(dict1))
print("===len函数===", end="\n\n")

# todo 1.6.14 str()
# 将字典转字符串
str1 = str(dict1)
print(f"值: {str1}, 类型: {type(str1)}")
print("===str函数===", end="\n\n")

# todo 1.7 字典推导式
alist = {x: x ** 2 for x in (2, 4, 6)}
print(f"字典推导式: {alist}")

# todo 1.8 遍历字典
for k, v in dict1.items():
    print(f"键: {k}, 值{v}")
