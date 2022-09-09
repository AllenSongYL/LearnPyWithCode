# -*- coding: utf-8 -*-
# @time:         2022/8/30 21:42
# @Author:       Alan
# @File:         interview_questions.py
# @Software:     PyCharm
# @Description:  面试题1 测试

# todo 1.0 一行代码实现1~100求和
print(sum(range(1, 101)))
print("===1~100求和===", end="\n\n")

# todo 1.1 字典如何删除键和合并两个字典
dict1 = {1: "a", 2: "b", 5: "e"}
dict2 = {3: "c", 4: "d"}

del dict1[5]

dict3 = dict1 | dict2
print()
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
print("===随机生成整数===", end="\n\n")

# todo 1.9 正则提取HTML标签中的内容
import re

print(re.findall(
    r'<div class=".*">(.*)</div',
    '<div class="nam">中国</div>'
))
print("===正则提取HTML标签中的内容===", end="\n\n")

# todo 1.10 断言
# assert 1 == 2
assert 1 == 1
print("===断言===", end="\n\n")

# todo 1.11  / python3 /
print(3 / 3)
print(10 // 3)
print("===/ 和 //===", end="\n\n")

# todo 1.12 对字符串去重并排序
s = "ajldjlajfdljfddd"
ss = list(set(s))
ss.sort()
print("-".join(ss))
print("===对字符串去重并排序===", end="\n\n")

# todo 1.13 用lambda函数实现两个数相乘
a = lambda x, y: x * y
print(a(12, 10))
print("===用lambda函数实现两个数相乘===", end="\n\n")

# todo 1.14 字典根据键大小排序
dic = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
resErr = sorted(dic)
print(resErr)
res = sorted(dic.items(), key=lambda x: x[0])
print(res)
print("===字典根据键大小排序===", end="\n\n")

# todo 1.15 字符串排序
b = list("feshja")
b.sort()
print("".join(b))
print("===字符串排序===", end="\n\n")

# todo 1.16 计算字符串中子串出现的次数
import collections

str1 = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
acounter = collections.Counter(str1)
print(acounter)
print("===字符串排序===", end="\n\n")

# todo 1.17 使用正则过滤字母和数字
a = "not 404 found 张三 99 深圳"
print(" ".join(re.findall(r"[^\W\da-zA-Z]+", a)))
print("===使用正则过滤字母和数字===", end="\n\n")

# todo 1.18 筛选出列表奇数并构造新列表
a = list(range(1, 10))
b = [i for i in filter(lambda x: x % 2 != 0, a)]
print(b)
print("===筛选出列表奇数并构造新列表===", end="\n\n")

# todo todo 1.19 判断以下类型
print(type((1,)))
print(type((1)))
print(type(("1")))
print("===判断以下类型===", end="\n\n")


# 二分查找
def binary_search(data_list, val):
    low = 0
    high = len(data_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_list[mid] == val:
            return mid
        elif data_list[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return None


print("===二分查找===", end="\n\n")

# todo 1.20 合并两个列表
a = [1, 5, 7, 9, 11]
b = [2, 4, 6, 8]
c = a + b
print(c)
# a.extend(b)
# print(a)
c = zip(a, b)
print(c, type(c))
for i in c:
    print(i)
print("===合并两个列表===", end="\n\n")

#  todo 1.21 展开二维列表
a = [[1, 2], [3, 4], [5, 6]]
b = [j for i in a for j in i]
print(b)
print("===展开二维列表===", end="\n\n")

#  todo 1.22 交换两个变量的值
a = 1
b = 2
print(f"a={a},b={b}")
a, b = b, a
print(f"a={a},b={b}")
print("===交换两个变量的值===", end="\n\n")

# todo 1.23 zip函数
a = [1, 2, 3]
b = [4, 5]
c = list(zip(a, b))
print(c, "\n", type(c))
for i in c:
    print(i)
print("===zip函数===", end="\n\n")

# todo 1.24 字符串转bytes，bytes转字符串
a = "hello"
b = a.encode()
print(b, type(b))
c = b.decode()
print(c, type(c))
print("===字符串转bytes，bytes转字符串===", end="\n\n")

# todo 1.25 保留两位小数
a = 1.3344
print(round(a, 2))
print("===保留两位小数===", end="\n\n")

# todo 1.26 字典和json字符串相互转换
import json

a = {"name": "zs", "age": 18}
b = json.dumps(a)
print(b, type(b))
c = json.loads(b)
print(c, type(c))
print("===字典和json字符串相互转换===", end="\n\n")

# todo 1.27 正则匹配中文
a = "张三 aaa 18 深圳".encode("utf-8").decode("utf-8")
print(re.findall(r"[\u4e00-\u9fff]+", a))
print("===正则匹配中文===", end="\n\n")

# todo 1.28 列表的交集，并集，差集
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print(list(set(a) & set(b)))
print(list(set(a) | set(b)))
print(list(set(a) - set(b)))
print(list(set(a) ^ set(b)))
print("===列表的交集，并集，差集===", end="\n\n")


# todo 1.29 闭包
def person(name):
    def say(y):
        print(f"{name}说：{y}")

    return say


f = person("张三")
l = person("李四")
print(f, type(f))
f("我是张三")
l("我是李四")
f("李四你好")
f("张三你好")


def base(x):
    def add():
        return x + 1

    return add


f = base(10)
print(f())
print(f())
print(f())
print("===闭包===", end="\n\n")

# todo 1.30 作用域
a = 1  # 全局变量


def func():
    a = 2  # 局部变量
    print(f"func中的a: {a}")

    def inner():
        nonlocal a
        a = 3
        print(f"inner中的a: {a}")

    inner()
    print(f"inner后的的a: {a}")


func()
print(f"func后的a: {a}")
print("===作用域===", end="\n\n")


# todo 1.31 新式类和旧式类
class Person(object):
    def __init__(self):
        pass

    def sayHello(self):
        print("hello, i am person")


class Man(Person):
    def __init__(self):
        pass

    def sayHello(self):
        print("hello, i am man")


class Woman(Person):
    def __init__(self):
        pass

    def sayHello(self):
        print("hello, i am woman")


class Child(Man, Woman):
    def __init__(self):
        pass

    def sayHello(self):
        print("hello, i am child")


child = Child()
child.sayHello()
print("===作用域===", end="\n\n")


# todo 1.32 实例方法，类方法，静态方法的区别
class Dog:
    # 类属性
    master = "张三"

    def __init__(self, name):
        self.name = name

    # 实例方法
    def eat(self):
        print(f"{self.name}在吃饭")

    # 类方法
    @classmethod
    def run(cls):
        print(f"{cls} {cls.master}  在跑")

    # 静态方法
    @staticmethod
    def sleep():
        print("在睡觉")


littleBlack = Dog("小黑")
littleBlack.eat()  # 实例调用eat实例方法
littleBlack.run()  # 实例调用run类方法
littleBlack.sleep()  # 实例调用sleep静态方法

Dog.run()  # 类调用run类方法
Dog.sleep()  # 类调用sleep静态方法
print("===实例方法，类方法，静态方法的区别===", end="\n\n")

# todo 1.33 判断列表是否为空
a = []
if a:
    print("列表不为空")
else:
    print("列表为空")
print("===判断列表是否为空===", end="\n\n")

# todo 1.34 调用外部命令
import subprocess

p = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(p.stdout.read().decode("utf-8"))
p1 = subprocess.run(['ping', 'www.baidu.com'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(p1.stdout.decode("utf-8"))


# todo
class myfun:
    pass
