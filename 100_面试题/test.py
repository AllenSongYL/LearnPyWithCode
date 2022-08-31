# -*- coding: utf-8 -*-
# @time:         2022/8/30 21:42
# @Author:       Alan
# @File:         test.py
# @Software:     PyCharm
# @Description:  面试题1 测试

# todo 1.0 一行代码实现1~100求和
print(sum(range(1, 101)))
print("===1~100求和===", end="\n\n")

# todo 1.1 字典如何删除键和合并两个字典
dict1 = {1: "a", 2: "b", 5: "e"}
dict2 = {3: "c", 4: "d"}

del dict1[5]

dict1.update(dict2)
print(dict1)
dict1 |= dict2
print(dict1)
print("===删除键和合并两个字典===", end="\n\n")

# todo 1.2 列表去重
list1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
list2 = list(set(list1))
print(list2)
print("===列表去重===", end="\n\n")


# todo 1.3 *args 和 **kwargs
def test(*args, **kwargs):
    print(f"args: {args}, type: {type(args)}")
    print(f"kwargs: {kwargs}, type: {type(kwargs)}")


print(test(1, 2, 3, 4, 5, a=1, b=2, c=3))
print("===*args 和 **kwargs===", end="\n\n")

# todo 1.4 内置数据类型
print(type(100))
print(type(0.1))
print(type(1.5j))
print(type(True))
print(type("True"))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({1: "a", 2: "b", 3: "c"}))
print(range(1, 10), type(range(1, 10)))
print("===内置数据类型===", end="\n\n")

# todo 1.5 面向对象中__init__和__new__的区别
# __init__是初始化方法，创建对象后，就立即被默认调用
# __new__是实例化方法，创建对象时，第一个被默认调用
# __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，
# 可以return父类（通过super(当前类名, cls)）__new__出来的实例，或者直接是object的__new__出来的实例
class Person:
    def __init__(self, name, age):
        print("__init__")
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super().__new__(cls)


aPerson = Person("Alan", 18)
print(f"aPerson.__init__: {aPerson.__init__}\naPerson.__new__: {aPerson.__new__}")
print("===__init__和__new__的区别===", end="\n\n")

# todo 1.6  with语句打开文件
# with open() as f: 语句会自动调用close()方法，不需要手动调用
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("使用with打开文件，并写入这行文字!")

# 对比open()方法
try:
    f = open("test.txt2", "r", encoding="utf-8")
    print(f.read())
except:
    print("文件不存在")
finally:
    if f:
        f.close()

print("===with方法，打开文件===", end="\n\n")

# todo 1.7 map()和列表推导式
list3 = [1, 2, 3, 4, 5]
result1 = list(map(lambda x: x ** 2, list3))
print(result1)
result2 = [i for i in result1 if i > 10]
print(result2)
print("=== map()和列表推导式===", end="\n\n")

# todo 1.8 随机生成整数，和0-1之间的小数
import random
print(random.randint(0, 100))
print(random.random())