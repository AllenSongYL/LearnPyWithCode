# -*- coding: utf-8 -*-
# @time:         2022/8/30 16:58
# @Author:       Alan
# @File:         p4_sorted.py
# @Software:     PyCharm
# @Description:  sorted函数

"""
sorted 函数
返回一个新列表，其中包含从可迭代中升序排列的所有项目。
可以提供自定义键函数来自定义排序顺序，并且可以设置反向标志以按降序请求结果。

sorted函数也是一个高阶函数，可以接受一个key函数来定制排序规则。
key 指定排序的对象，可以传入函数或方法名，这样可以把函数作为排序的标准。
reverse 可选参数，默认为False，表示升序排列，如果为True，则表示降序排列。

list.sort(key=None, reverse=False)
会改变原列表，而不是返回一个新的列表。节约内存。
"""

a1 = [36, 5, -12, 9, -21]
print(sorted(a1))

# 可以指定key函数来定制排序规则
# 使用abs绝对值函数来定制排序规则
print(sorted(a1, key=abs))

print(sorted(a1, key=lambda x: -x))

# 可以通过字典的keys来定制排序规则
array = [{"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
print(sorted(array, key=lambda x: x["age"]))

# 多列排序
# 先通过成绩，降序排列，再通过姓名，升序排列
d1 = [{'name': 'alice', 'score': 38}, {'name': 'bob', 'score': 18}, {'name': 'darl', 'score': 28},
      {'name': 'christ', 'score': 28}, {'name': 'coco', 'score': 38}]
print(sorted(d1, key=lambda x: (-x['score'], x['name'])))
