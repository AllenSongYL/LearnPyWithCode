# -*- coding: utf-8 -*-
# @time:         2022/8/26 11:11
# @Author:       Alan
# @File:         p1_string.py
# @Software:     PyCharm
# @Description:  基本数据类型 -  字符串

# todo 1.0 字符串类型
"""
最常用的数据类型。可以使用双引号或单引号创建字符串

特性
- 不可变

操作运算符
+          字符串拼接
*          重复输出
[]         通过索引获取获取字符串
in         成员运算符 - 如果字符串中包含给定的字符返回 True
not in     成员运算符 - 如果字符串中不包含给定的字符返回 True
"""


# 定义字符串
aString = "张三"
print(aString)
# 使用type()查看数据类型
print(type(aString))

# 值传递，bString改变不会影响aString
bString = aString
bString = bString + "和李四"
print(aString)
print(bString)

# todo 1.1 字符串运算符
# 拼接字符串
print("abcd" + "ABCD")

# 重复输出
cString = "A"
dString = cString * 10
print("cString * 10 = ", dString)

# in 运算符 返回True或False
eString = "0123456"
print("in 成员运算符，返回结果： ", "2" in eString)
print("in 成员运算符，返回结果： ", "8" in eString)
print("not in 成员运算符，返回结果： ", "2" not in eString)
print("not in 成员运算符，返回结果： ", "8" not in eString)
print("===字符串运算符===", end="\n\n")

# todo 1.2 使用索引
# 起始索引从0开始,从左往右0,1,2......;从右往左-1,-2,-3......
# 左闭右开 结尾索引为6，[:6]时不输出最后字符
# 起始索引0，结束索引-1 可以省略
# [::2] 指定步长值
print("eString[4] : ", eString[4])
print("eString[2:4] : ", eString[2:4])
print("eString[:4] :", eString[:4])
print("eString[3:] :", eString[3:])
print("eString[:6] :", eString[:6])
print("eString[-3:-1] :", eString[-3:-1])
print("eString[-3:0] : ", eString[-3:])
print("eString[::2] : ", eString[::2])
print("===使用索引===", end="\n\n")

# todo 1.3 字符串内建函数
fString = "this is a long string~~~!"
# todo 1.3.1 capitalize() 首字母大写
print("capitalize()方法: ", fString.capitalize())
print("===使用capitalize===", end="\n\n")

# todo 1.3.2 center(width, char)
# 第一个参数指定长度，第二个参数指定单个字符
print("center()方法: ", fString.center(50, "="))
print("===使用center===", end="\n\n")

# todo 1.3.3 count(str, [begin], [end])
# 统计指定str在string中出现的次数
print(fString.count("s"))
print(fString.count("is", 0, 5))
print("===使用count===", end="\n\n")

# todo 1.3.4 encode(encoding, [errors])
# 以指定的编码格式编码字符串。
gString = "编码方法！！！"
encodeUTF8 = gString.encode(encoding="UTF-8", errors="strict")
print(encodeUTF8)
encodeGBK = gString.encode(encoding="GBK")
print(encodeGBK)
print("===使用encode编码===", end="\n\n")

# todo 1.3.5 bytes.decode(encoding, [errors])
# 以指定的编码格式解码bytes对象，默认"UTF-8". 返回值：解码后的字符串。
print("decode UTF-8: ", bytes.decode(encodeUTF8))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 0: invalid start byte
# print("decode GBK: ", bytes.decode(encodeGBK))
print("===使用bytes.decode解码===", end="\n\n")

# todo 1.3.6 endswith(str, [start], [end])
# 判断字符串是否以指定后缀结尾。是则返回True，否则返回False。
# str   指定结尾字符串或元素
# start 字符串中的起始位置
# end   字符串中的结束位置
# startswith 相似 检查字符串是否以指定子字符串substr开头
print(gString.endswith("！"))
print(gString.endswith("编"))
print(gString[:4])
print(gString.endswith("法", 0, 4))
print("===使用endswith===", end="\n\n")

# todo 1.3.7 find(str, [start], [end])
# 查看字符串中是否包含str。返回第一个匹配的子str的索引位置，不包含返回-1
# start 字符串中的起始位置
# end   字符串中的结束位置
# 对应rfind，和find相似，从右开始查找
tString = "aaabbbcccee"
print(tString)
print("find(\"a\"): ", tString.find("a"))
print("find(\"bbb\"): ", tString.find("bbb"))
print("find(\"f\"): ", tString.find("f"))
print("find(\"c\"): ", tString.find("c", 7, -1))
print("find(\"ee\"): ", tString.find("ee", 4))
print("===使用find===", end="\n\n")

# todo 1.3.8 index(str, [start], [end])
# 和find方法一样。
# 对应rindex, 和index相似，从右开始索引
print("index(\"a\"): ", tString.index("a"))
print("index(\"bbb\"): ", tString.index("bbb"))
# 当str不在字符串中会报错： ValueError: substring not found
# print("index(\"f\"): ", tString.index("f"))
print("===使用index===", end="\n\n")

# todo 1.3.9 isdigit()
# 判断字符串是否只包含数字。是则返回True，否则False
print(tString.isdigit())
print("1234444".isdigit())
print("123 4444".isdigit())
print("===使用isdigit===", end="\n\n")

# todo 1.3.10 join(iter)
# 指定可迭代的对象，使用字符串作为分隔符生产新字符串
hString = "-"
hStringNew = hString.join(["0", "1", "3"])
print(hStringNew)
print(type(hStringNew))
print(hString.join("abcdefg"))
print("===使用join===", end="\n\n")

# todo 1.3.11 len(obj)
# 返回对象(字符串，列表，元素等)长度或项目个数
print(len(tString))
print(len([0, 2, 1, 3]))
print("===使用len===", end="\n\n")

# todo 1.3.12 ljust(width, [fillstr])
# 向左对其，并使用指定单个字符填充，不指定默认为空格
# 指定长度小于原字符串，则直接返回原字符串
# 对应 rjust方法。向右对其，使用方法和ljust一致。
ljustString = "abc"
print(f"{ljustString.ljust(10)}|")
print(ljustString.ljust(10, "T"))
print(ljustString.ljust(2, "T"))
print(f"{ljustString.rjust(10)}|")
print(ljustString.rjust(10, "T"))
print("===使用ljust/rjust===", end="\n\n")


# todo 1.3.13 replace(old, new, [max])
# 将字符串中old替换为new，max指定替换个数，不指定则替换全部。
print(tString)
print(tString.replace("a", "A"))
print(tString.replace("a", "A", 2))
print("===使用replace===", end="\n\n")

# todo 1.3.14 max()
# 返回字符串中最大的 字母对应码值
# 对应min 返回最小的
maxString ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print(max(maxString))
print(min(maxString))
print("===使用max/min===", end="\n\n")

# todo 1.3.15 split(str, [count])
# 通过指定分隔符对字符串进行切片;count指定分割的个数，默认全部
# 返回一个list
splitString = "a|b|c|d|e"
splitStringReturn = splitString.split("|")
print(splitStringReturn)
print(type(splitStringReturn))
splitString2 = "eaafaagaahaajaa"
print(splitString2.split("aa"))
print(splitString2.split("aa", 2))
print("===使用split===", end="\n\n")

# todo 1.3.16 splitlines(keepends=False)
# 按照('\r', '\r\n', '\n')分隔，返回一个list列表类型
# keepends默认为False，返回list不包含换行符。指定True，包含换行符
slString = "abcd\refgh\nijkl\r\nmnop\rqrst\n\nuvwx"
print(slString.splitlines())
print(type(slString.splitlines()))
print(slString.splitlines(True))
print("===使用splitlines===", end="\n\n")

# todo 1.3.17 strip([char])
# 不指定默认去除字符串左右两边的空白字符(\n, \r, \t, ' ')，指定则去除指定的字符，左右两边直到遇到第一个不包含在其中的字符为止
# rstrip和lstrip相似；rstrip：删除末尾空白字符或指定的多个字符；lstrip： 删除开头空白字符或指定的多个字符
stripString = "  a bcc dd   "
print(f"|{stripString}|")
print(f"|{stripString.strip()}|")
stripString2 = "**123**456**789****"
print(f"|{stripString2}|")
print(f'|{stripString2.strip("*")}|')
stripString3 = "123444421"
print(f'|{stripString3}|')
print(f'|{stripString3.strip("12")}|')
stripString4 = '12313223121332131277321312213231123132'
print(stripString4.strip('123'))
print("===使用strip===", end="\n\n")

# todo 1.3.18 swapcase()
# 大写转小写，小写转大写
scString = "ABCDeee"
print(scString.swapcase())
print("===使用swapcase===", end="\n\n")

# todo 1.3.19 title()
# 返回标题化的字符串，每个单词首字母大写，其余小写
titleString = "this is a VERY long strings!!!"
print(titleString.title())
print("===使用title===", end="\n\n")

# todo 1.3.20 upper()
# 小写字母转大写
lowString = "aABbcC"
print(lowString.upper())

# todo 1.3.21 zfill(width)
# 返回指定长度的字符串，用0补齐
# 可以使用rjust代替
zfillSting = "abc"
print(zfillSting.zfill(30))
