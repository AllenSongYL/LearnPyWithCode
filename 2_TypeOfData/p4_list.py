# -*- coding: utf-8 -*-
# @time:         2022/8/27 21:20
# @Author:       Alan
# @File:         p4_list.py
# @Software:     PyCharm
# @Description:  list 列表

# todo 1.0 list列表
"""
序列中每个值都有相对应的位置值，称为索引。
使用"[]"创建，元素之间用都好分隔
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
alist = ['a', 'b', 5, 10, True, 4.5, [0.5, False], None]
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

# todo 1.5 检查元素是否在列表中
if 4.5 in alist:
    print("YES! 4.5 in list!")

# todo 1.6 列表方法
print(alist)
# todo 1.6.1 appen()  在末尾追加
alist.append("append方法")
print(f"alist.append(\"append方法\") = {alist}")
alist.append(['777', '888'])
print(f"alist.append(['777', '888']) = {alist}")

# todo 1.6.2 insert 在指定索引位插入
alist.insert(1, '444')
print(f"alist.insert(1, '444') = {alist}")

# todo 1.6.3 extend  拼接两个列表
alist.extend(['e', 'x', 't', 'e', 'n', 'd'])
print(f"alist.extend(blist) = {alist}")

# todo 1.6.4 + 运算符 拼接列表
# 会返回一个新的list对象，需要接收，需要消耗额外的内存，不推荐
alist = alist + [1, 4]
print(f"alist + [1, 4] = {alist}")

# todo 1.6.3 remove()  删除列表中指定元素
alist.remove(10)
print(f"alist.remove(10) = {alist}")

# todo 1.6.4 pop([index])  删除指定位置的元素
# 不指定索引，默认删除最后一个
alist.pop()
print(f"alist.pop() = {alist}")
alist.pop(0)
print(f"alist.pop(0) = {alist}")