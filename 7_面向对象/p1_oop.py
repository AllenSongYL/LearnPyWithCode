# -*- coding: utf-8 -*-
# @time:         2022/8/30 10:59
# @Author:       Alan
# @File:         p1_oop.py
# @Software:     PyCharm
# @Description:  面向对象编程
from types import MethodType

# todo 1.0 面向对象介绍
"""
将程序推理为一组对象，而不是一组操作
对象：        包含状态和行为的实体;是结合数据和代码的实体；一个对象封装一个状态，然后提供方法来操作该状态，并与之交互。
状态：        存储在对象中的一组数据(内部数据)
行为：        对象可以执行的操作集合

比如有一个"人"的类，状态有: 姓名、年龄、身高、体重等；行为: 唱歌、跳舞、rap、打篮球等
使用该类实例化一个确实的对象, 如蔡徐坤，拥有明确的姓名,年龄等状态信息，同时具有各种人这个类的行为。

类(Class):   用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。
类的组成
- 属性       存储在每个对象中的数据；对象内部的变量，构成其内部状态的一部分
- 构造函数    在创建对象时初始化对象的代码; 使用特殊名称: __init__
- 方法       每个对象可以执行的行为；一个可以对该对象进行操作的内部函数
- 封装       保护对象的数据不受外部访问


类变量：      类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：    类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：    如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
实例变量：    在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
"""


# todo 1.1 创建和使用类
# 使用class关键字定义一个类
# 类型通常首字母大写
class Person:
    # 定有类的属性
    classname = 'p'

    # 构造方法，该方法在类实例化时自动调用
    # 第一个参数必须是self，self代表创建的实例本身，而非类
    # 将传入的参数，实例化到具体的对象上
    # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数
    def __init__(self, name, age, hobby, height):
        # 以下直接构造方法无法实例化对象的属性进行判断
        print("执行__init__构造方法")
        # 定义成员属性
        self.name = name
        self.age = age
        # 前面单下划线(_)的属性，表示受保护的属性
        # 不建议直接访问
        self._hobby = hobby
        # 前面单下划线(__)的属性，表示私有属性
        # 只能内部访问，外部无法访问
        self.__height = height

        # 可以调用一个方法来实例化
        # self.set_person(name, age)

    def getattr(self):
        return self

    # 定义一个实例方法
    # 需要实例化一个对象后调用
    # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
    def hello(self):
        print(f"大家好，我叫{self.name}, 今年{self.age}岁了!")

    # @staticmethod装饰器，指定下面的方法为静态方法，通过类名.方法名可以直接调用
    @staticmethod
    def cry():
        print("i am cry")

    def like(self):
        # 内部可以访问私有属性
        print(f"我的爱好是: {self._hobby}")

    # 可以添加一个get方法来访问私有属性
    def get_hobby(self):
        return self._hobby

    # 可以创建一个set方法来修改私有属性
    def set_hobby(self, hobby):
        self._hobby = hobby

    def get_height(self):
        return self.__height

    # 可以对传入的参数进行检查，避免传入无效参数
    def set_height(self, height):
        if type(height) == int:
            self.__height = height
        else:
            raise ValueError("please enter a int")

    # 使用@property语法糖 只读获取属性的值
    @property
    def hobby(self):
        return self._hobby

    @hobby.setter
    def hobby(self, hobby):
        # 改用set_person方法进行set
        # self._hobby = hobby
        self.set_person(self.name, hobby)

    def set_person(self, name, age):
        if type(self.age) != int:
            raise ValueError("please enter int")
        elif self.age > 120 or self.age < 0:
            raise ValueError("please enter 0~120")
        else:
            self.age = age
        if type(self.name) != str:
            raise ValueError("please enter str")
        else:
            self.name = name


# 实例化一个对象 使用__init__构造方法
# 现在内存中创建一个新的Person对象，执行构造方法，引用新创建的对象作为self，并将'alan'和27两个属性传递给self
a1 = Person('alan', 27, 'play ganmes', 190)
print(f"类 {Person}")
print("---")
a1.hello()
Person.cry()
a2 = Person('jon', 18, 'fly', 178)
# 不同实例的内存地址不同
print(f"实例对象 a1: {a1}\n实例对象 a2: {a2}")
# 可以随意访问和修改实例对象的属性
print(a1.name)
a1.name = "papa"
print(a1.name)
print("===实例化对象===", end="\n\n")

# todo 1.2 封装
# 访问受保护的属性
print(f"a1._hobby = {a1._hobby}")
a1._hobby = "打篮球"
print(f"get方法: {a1.get_hobby()}")

# 调用set方法修改私有属性
a1.set_hobby("游泳")
print(a1.get_hobby())

print("===受保护的属性===", end="\n\n")

# 访问私有属性
# 外部无法访问私有属性
# 私有属性被自动结成成_类名__私有属性名
print(a1._Person__height)
a1.set_height(178)
print(a1.get_height())
print("===私有属性===", end="\n\n")

# 使用@property装饰器后，可以直接访问hobby，但是不能修改
# 把一个方法变成属性调用;把一个getter方法变成属性，只需要加上@property
# 此时还会生成另一个装饰器 属性名.setter，负责把一个setter方法变成属性赋值
print(a1.hobby)
a1.hobby = "听音乐"
print(a1.hobby)
print("===封装===", end="\n\n")

# todo 1.3 继承和多态
"""
子类继承了父类全部的功能
子类可以重写父类的方法
开闭原则
对扩展开放：允许新增Animal子类；
对修改封闭：不需要修改依赖Animal类型的函数。

静态语言 vs 动态语言
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，
都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，
完全可以传入任何实现了read()方法的对象。
"""


#

class Animal:
    def run(self):
        print("动物在奔跑!")


class Cat(Animal):
    def eat(self):
        print("吃鱼!")


class Dog(Animal):
    def eat(self):
        print("吃骨头")

    # 重写父类的run方法；override(重写)
    def run(self):
        print("狗狗自由奔跑!")


# 实例化一个猫对象
# 调用父类的run方法
cata = Cat()
# 可以调用父类的方法
cata.run()
cata.eat()
print("===")
doga = Dog()
doga.run()
doga.eat()
print("===继承===", end="\n\n")

print(f"isinstance(doga, Animal) = {isinstance(doga, Animal)}")
print(f"isinstance(doga, Dog) = {isinstance(doga, Dog)}")
print(f"isinstance(doga, Cat) = {isinstance(doga, Cat)}")

aanimal = Animal()
print(f"isinstance(aanimal, Dog) = {isinstance(aanimal, Dog)}")
print(f"isinstance(aanimal, Animal) = {isinstance(aanimal, Animal)}")
print("===多态===", end="\n\n")

# todo 1.4 dir()
# 获取一个对象所有的属性和方法,返回一个列表
# ___xxx___的属性和方法是Python中的特殊属性或方法
print(dir(a1))
print(type(dir(a1)))

# len()函数获取对象的长度，实际上内部调用的__len__()方法
print(len("abc") == "abc".__len__())
print("===dir()===", end="\n\n")


# todo 1.5 gettar/setattr/hasattr
# 内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
# 要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。否则直接可以使用 对象.属性
class T1:
    def __init__(self):
        self.name = 'momo'

    def upp(self):
        self.name = self.name.upper()


t1 = T1()
# hasattr(对象, 属性名) 判断该对象是否有指定属性
print(hasattr(t1, 'name'))

# setattr(对象, 属性名, 值) 设定实例对象属性的值
setattr(t1, 'name', 'newname')
print(t1.name)

# getattr(对象, 属性名) 获取实例对象属性的值
print(getattr(t1, 'name'))


# todo 1.6 动态添加方法
def dynamicMethod(self):
    print("给实例动态添加方法")


t1.dynamicMethod = MethodType(dynamicMethod, t1)
t1.dynamicMethod()
print(dir(t1))
# 仅对当前实例有效；要对所有实例绑定方法，可以给class绑定方法
T1.dynamicMethod = dynamicMethod
print(dir(T1))
print("===动态添加方法===", end="\n\n")


# todo 1.7 __slots__
# 限制属性
# 用元组定义允许绑定的属性名称
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class Student:
    __slots__ = ('name', "age")


s = Student()
s.name = 'ppap'
s.age = 100
# 无法添加属性 AttributeError: 'Student' object has no attribute 'score'
# s.score = 100
# 由于score没有被添加到__slots__中，所以不能绑定该属性

# todo 1.8 多重继承
"""
通过多重继承，一个子类就可以同时获得多个父类的所有功能。
"""


class A(Person, Student):
    pass


# todo 1.9 魔术方法
"""
__str__(): 自定义打印时的内容
__repr__():交互模式时，输出的字符串
__iter__(): 如果要被for...in循环，必须实现该方法，该方法返回一个迭代对象
__next__(): 然后for会调用该方法不停拿到下一个值，知道遇到StopIteration
__getitem__(): 像list一样按照下标取元素，需要实现该方法
__getattr__(): 调用不存在的属性时，会调用该方法来尝试获取属性
__call__(): 直接对实例进行调用

"""


class Bird:

    def __init__(self, name):
        self.name = name

    # print输出的内容
    def __str__(self):
        return f"鸟类! {self.name}"

    # 交互模式时，输出的字符串
    # def __repr__(self):
    #     return f"鸟类! {self.name}"
    # 一般和__str__一样
    __repr__ = __str__


a3 = Bird('乌鸦')
print(a3)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


for i in Fib():
    print(i)