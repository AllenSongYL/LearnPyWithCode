# -*- coding: utf-8 -*-
# @time:         2022/8/31 8:27
# @Author:       Alan
# @File:         p8_bytes&bytearry.py
# @Software:     PyCharm
# @Description:  Python bytes & bytearray 类型

# todo 1.0 bytes 介绍
# bytes类型
"""
bytes 类型用来表示一个字节串。由单个字节构成的不可变序列.
bytes 是 Python 3.x 新增的类型，在 Python 2.x 中是不存在的。
bytes 类型的变量可以被视为一个 list，但每个元素都是一个 int 值，而不是一个字符。
bytes 只负责以字节序列的形式（二进制形式）来存储数据，至于这些数据到底表示什么内容（字符串、数字、图片、音频等），完全由程序的解析方式决定。
如果采用合适的字符编码方式（字符集），字节串可以恢复成字符串；反之亦然，字符串也可以转换成字节串。

字节串（bytes）和字符串（string）的对比：
字符串由若干个字符组成，以字符为单位进行操作；字节串由若干个字节组成，以字节为单位进行操作。
字节串和字符串除了操作的数据单元不同之外，它们支持的所有方法都基本相同。
字节串和字符串都是不可变序列，不能随意增加和删除数据。

字节串和字符串都是可迭代的，可以使用 for 循环来遍历。
如果字符串的内容都是 ASCII 字符，那么直接在字符串前面添加 b前缀 就可以转换成 bytes。
bytes 是一个类，调用它的构造方法，也就是 bytes()，可以将字符串按照指定的字符集转换成 bytes；如果不指定字符集，那么默认采用 UTF-8。
字符串本身有一个 encode() 方法，该方法专门用来将字符串按照指定的字符集转换成对应的字节串；如果不指定字符集，那么默认采用 UTF-8。

对于非 ASCII 字符，print 输出的是它的字符编码值（十六进制形式），而不是字符本身。
非 ASCII 字符一般占用两个字节以上的内存，而 bytes 是按照单个字节来处理数据的，所以不能一次处理多个字节。
"""

# todo 1.0 创建bytes
# 创建一个字节串
bt1 = b"hello"
print(f"bt1 = {bt1},type(bt1) = {type(bt1)}")
# 使用构造函数创建
bt2 = bytes(range(1, 10))
print(f"bt2 = {bt2},type(bt2) = {type(bt2)}")
print("===字节串的创建===", end="\n\n")



# todo 1.1 字节串、字符串的转换
# 字节串的操作
str1 = "hello 字符串"
bt3 = bytes(str1, encoding="utf-8")
print(bt3, len(bt3))
print("===字符串转字节串===", end="\n\n")

str2 = bt3.decode("utf-8")
print(f"str2 = {str2},type(str2) = {type(str2)}")
print("===字节串转字符串===", end="\n\n")

# todo 1.2 for循环
for i in bt3:
    print(i)
print("===字节串for循环===", end="\n\n")

# todo 2.0 bytearray 介绍
#
"""
bytearray对象是bytes对应的可变对象;是一个可变序列
包含范围为 0 <= x < 256 的整数。

没有专属的字面值语法，它们总是通过调用构造器来创建
bytearray([source], [encoding], [errors])    返回一个新的 bytes 数组

如果是一个 string，您必须提供 encoding 参数（errors 参数仍是可选的）；
bytearray() 会使用 str.encode() 方法来将 string 转变成 bytes。
果source是一个 integer，会初始化大小为该数字的数组，并使用 null 字节填充。
如果是一个遵循 缓冲区接口 的对象，该对象的只读缓冲区将被用来初始化字节数组。

创建一个空实例: bytearray()
创建一个指定长度的以零值填充的实例: bytearray(10)
通过由整数组成的可迭代对象: bytearray(range(20))
通过缓冲区协议复制现有的二进制数据: bytearray(b'Hi!')
"""

# source为字符串时，必须指定encoding
# 否则报错: TypeError: string argument without an encoding
# bytearray() 会使用 str.encode() 方法来将 string 转变成 bytes。
ba1 = bytearray("hello  你好呀", encoding="utf-8")
print(f"ba1 = {ba1}, type(ba1) = {type(ba1)}")
for i in ba1:
    print(i)
print("===bytearray(str)===", end="\n\n")

# 如果source是一个 integer，会初始化大小为该数字的数组，并使用 null 字节填充。
ba2 = bytearray(10)
print(ba2)
for i in ba2:
    print(i)
print("===bytearray(int)===", end="\n\n")

# 使用bytes来创建bytearray
ba3 = bytearray(b'Hi!')
for i in ba3:
    print(i)
print(f"ba3 = {ba3}, type(ba3) = {type(ba3)}")


str3 = "fff 你好呀!"
ba4 = bytearray(bytes(str3, encoding="utf-8"))
for i in ba4:
    print(i, end=" ")

print(f"\nlen(str3) = {len(str3)}")
print(f"ba4 = {ba4}, type(ba4) = {type(ba4)}, len(ba4) = {len(ba4)}")
print("===bytearray(bytes)===", end="\n\n")

#
ba5 = bytearray(range(10))
print(f"ba5 = {ba5}, type(ba5) = {type(ba5)}")
for i in ba5:
    print(i)
# 超出范围报错 ValueError: byte must be in range(0, 256)
# ba6 = bytearray(range(260))
# print(f"ba6 = {ba6}, type(ba6) = {type(ba6)}")