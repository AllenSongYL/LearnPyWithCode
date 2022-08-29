# -*- coding: utf-8 -*-
# @time:         2022/8/27 21:20
# @Author:       Alan
# @File:         p4_list.py
# @Software:     PyCharm
# @Description:  list 列表

import copy
import operator

# todo 1.0 list列表
"""
序列中每个值都有相对应的位置值，称为索引。
使用"[]"创建，元素之间用逗号分隔
- 特点
    - 有序
    - 可变
    - 允许重复成员
    - 可包含任意数据类型
- 索引
    - 从左往右，从0开始，左闭右开
    - 从右往左，从-1开始，-2，-3，-4以此类推
    - [位置索引] 取单个元素
    - [起始位置:结束位置:步长值]
"""

# todo 1.1 创建列表
alist = ['a', 'b', 5, 10, True, 4.5, [0.5, False], None, 5]
print(f"列表: {alist}, 类型: {type(alist)}")

# todo 1.2 使用索引
print(f"alist[4] = {alist[4]}")
print(f"alist[1:4] = {alist[1:4]}")
print(f"alist[-4:-1] = {alist[-4:-1]}")
print(f"alist[6][0] = {alist[6][0]}")
print(f"alist[::2] = {alist[::2]}")
print("===通过索引index获取值===", end="\n\n")

alist[1] = 'ccc'
print(alist)
del alist[1]
print(f"通过del关键字删除指定索引的元素: \n{alist}")
print("===通过索引index修改值===", end="\n\n")

# todo 1.3 拷贝, 引用传递，传递地址值
blist = alist
print(f"alist内存地址: {id(alist)}, blist内存地址: {id(blist)}")
blist.append("new")
print(f"对blist进行追加会影响\nalist: {alist}\nblist: {blist}")
print(f"追加后alist内存地址: {id(alist)}, blist内存地址: {id(blist)}")

# 通过[:]可以拷贝值，
clist = alist[:]
print(f"alist内存地址: {id(alist)}, clist内存地址: {id(clist)}")
clist.append("new")
print(f"alist: {alist}\nclist: {clist}")

# todo 1.4 遍历列表
# 使用for in 循环取出列表中所有元素
for i in alist:
    print(i)

# todo 1.5 列表方法
print(alist)
# todo 1.5.1 appen()  在末尾追加
alist.append("append方法")
print(f"alist.append(\"append方法\") = {alist}")
alist.append(['777', '888'])
print(f"alist.append(['777', '888']) = {alist}")

# todo 1.5.2 insert 在指定索引位插入
alist.insert(1, '444')
print(f"alist.insert(1, '444') = {alist}")

# todo 1.5.3 extend  拼接两个列表
alist.extend(['e', 'x', 't', 'e', 'n', 'd'])
print(f"alist.extend(blist) = {alist}")

# todo 1.5.3 remove()  删除列表中指定元素
alist.remove(10)
print(f"alist.remove(10) = {alist}")

# todo 1.5.4 pop([index])  删除指定位置的元素
# 不指定索引，默认删除最后一个(-1)
# 返回删除的值
alist.pop()
print(f"alist.pop() = {alist}")
alist.pop(0)
print(f"alist.pop(0) = {alist}")

# todo 1.5.5 len(list)
# 返回列表的长度
print(f"len(alist) = {len(alist)}")

# todo 1.5.6 lsit(tunple)
# 将元组转为列表
print(f"list((1,2,3)) = {list((1, 2, 3))}")
print("===lsit()===", end="\n\n")

# todo 1.5.7 index(element)
# 返会列表中第一的匹配元素的索引
print(f"alist.index(True) = {alist.index(True)}")
print("===index()===", end="\n\n")

# todo 1.5.8 reverse()
# 返回None。反转列表顺序。
alist.reverse()
print(f"alist.reverse() = {alist}")
print("===reverse()===", end="\n\n")

# todo 1.5.9 sort()
# 返回None; 默认升序排序 reverse=False;reverse=True时，降序排序
blist = [65, 77, 23, 99]
blist.sort()
print(f"blist.sort() = {blist}; 返回值: {blist.sort()}")
clist = ["att", "acc", "edd", "uii", "baa", "中"]
clist.sort(reverse=True)
print(clist)
print("===sort()===", end="\n\n")

# todo 1.5.10 copy()
# 复制列表 值复制，非地址复制;
# 浅拷贝: 拷贝父对象，不会拷贝对象的内部的子对象。
dlist = alist.copy()
print(f"alist地址值: {id(alist)}; alist: {id(dlist)};")
print(f"alist[7]地址值: {id(alist[7])}; alist[7]: {id(dlist[7])};")
print(f"dlist[5]!!! = {dlist[5]}")
dlist[5].append("copy")
print(f"alist = {alist},\nblist = {dlist}")
print("===copy()===", end="\n\n")

# todo 1.5.11 deepcopy()
# 深拷贝: copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象
elist = copy.deepcopy(alist)
print(f"alist地址值: {id(alist)}; elist: {id(elist)};")
elist[5].append("deepcopy")
print(f"alist = {alist},\nblist = {elist}\n对拷贝对象进行修改不会影响原对象")
print("===deepcopy()===", end="\n\n")

# todo 1.5.12 clear()
# 清空列表
alist.clear()
print(f"alist.clear() = {alist}")
print("===clear()===", end="\n\n")


# todo 操作符
# todo 1.6.1 + 操作符
# 拼接列表，会返回一个新的list对象，需要接收，需要消耗额外的内存，不推荐
alist = ["a", "b"]
alist = alist + [1, 4]
print(f"alist + [1, 4] = {alist}")
print("===+ 操作符===", end="\n\n")

# todo 1.6.1 * 操作符
# 重复，不改变原列表，返回新列表,需要变量接收
flist = [1, 2, 3]
print(flist * 3)
print(flist)
glist = flist * 3
print(glist)
print("===* 操作符===", end="\n\n")

# todo 1.6.3 检查元素是否在列表中
if 4.5 in alist:
    print("YES! 4.5 in list!")
print("===in 操作符===", end="\n\n")

# todo 1.7 判断两个列表是否相等
hlist = [1, 2]
ilist = [1, 2]
jlist = [1, 3]
print(id(hlist), id(ilist))
print(f"{hlist} == {ilist} : {hlist == ilist}")
print(f"{hlist} == {jlist} : {hlist == jlist}")

# todo 列表比较 使用operator的方法
# 比较第一个元素，是则返回True，否则False,相等则比较第二个元素
print(f"{hlist} 小于 {jlist} : {operator.lt(hlist, jlist)}")
print("===列表比较===", end="\n\n")

# todo 1.8 列表推导式
# 从一个数据序列构建另一个新的数据序列的结构体
# 格式： [表达式 for 变量 in 列表 [if 条件]]
#       [结果值1 if 判断条件 else 结果2  for 变量名 in 原列表]
# 返回:  列表
xlist = [i for i in range(10) if i % 2 == 0]
print(f"[i for i in range(10) if i % 2 == 0] = {xlist}")

list1 = ['python', 'test1', 'test2']
list2 = [word.title() if word.startswith('p') else word.upper() for word in list1]
print(list2)

# 嵌套的列表推导式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
list3 = [[row[i] for row in matrix] for i in range(4)]
print(list3)
print("===列表推导式===", end="\n\n")
