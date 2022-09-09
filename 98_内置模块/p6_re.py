# -*- coding: utf-8 -*-
# @time:         2022/9/1 9:13
# @Author:       Alan
# @File:         p6_re.py
# @Software:     PyCharm
# @Description:  re 正则表达式

import re
import string

"""
compile 将正则表达式编译成正则表达式对象; 保存这个正则对象以便复用，可以让程序更加高效
match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败返回 None;匹配返回相应的匹配对象
fullmatch 匹配字符串的全部，如果字符串不符合正则表达式，则匹配失败返回 None;匹配返回相应的匹配对象
search 扫描整个字符串并返回第一个成功的匹配;如果没有匹配，就返回一个 None
findall 查找字符串中所有匹配正则表达式的子串，返回字符串列表
finditer 查找字符串中所有匹配正则表达式的子串，返回一个迭代器
split 通过正则表达式匹配分隔符，将字符串分割成列表
sub 用于替换字符串中的匹配项
split 用于分割字符串

匹配对象
group 返回一个或者多个匹配的子组。如果只有一个参数，结果就是一个字符串，如果有多个参数，结果就是一个元组（每个参数对应一个项）
groups 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号

. 匹配除了换行的任意字符
^ 匹配字符串的开始
$ 匹配字符串的结束
* 匹配前一个字符0次或者无限次
+ 匹配前一个字符1次或者无限次
? 匹配前一个字符0次或者1次
{n} 匹配前一个字符n次
{n,} 匹配前一个字符n次或者无限次
{n,m} 匹配前一个字符n到m次
| 匹配左右任意一个表达式
[] 匹配[]中列举的字符
[^] 不在[]中的字符
\d 匹配数字，即0-9
\D 匹配非数字，即不是数字
\s 匹配空白，即空格，tab键
\S 匹配非空白
\w 匹配单词字符，即a-z、A-Z、0-9、_
\W 匹配非单词字符
\b 匹配单词的开始或结束

* + ? {n} {n,} {n,m} 这些符号默认是贪婪匹配，也就是尽可能多的匹配字符
*? +? ?? {n,m}? 非贪婪模式，尽可能少的匹配


() 分组标记
(?P<name>) 分组标记，同时指定组名
(?P=name) 引用分组名为name匹配到的字符串


(...) 匹配括号内的表达式，也表示一个组
(?P<name>...) 分组并起别名
(?P=name) 引用别名为name分组匹配到的字符串
(?…) 匹配括号内的表达式，不表示一个组
(?:…) 匹配括号内的表达式，不表示一个组 匹配在括号内的任何正则表达式，但该分组所匹配的子字符串 不能 在执行匹配后被获取或是之后在模式中被引用。
(?#…) 注释
(?=…) 前向肯定界定符
(?!…) 前向否定界定符 当 … 不匹配时，匹配成功。
"""

# todo 1.0 re.compile()
"""
将正则表达式的样式编译为一个 正则表达式对象 （正则对象），可以用于匹配，通过这个对象的方法 match(), search() 和 findall() 来匹配字符串
re.compile(pattern, flags=0)
pattern 正则表达式字符串
flags 标志位，可以是0、re.I、re.M、re.S、re.U、re.X
re.I 忽略大小写
re.M 多行模式，影响 ^ 和 $
re.S 即为 . 匹配包括换行符在内的所有字符
re.U 支持Unicode
re.X 支持verbose语法
re.A 使 \w, \W, \b, \B, \d, \D, \s 和 \S 只匹配ASCII字符
"""

rexEmail = re.compile(r'[\w\d]+@[\w]+\.[\w]+')
rexPhone = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
rexDate = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
rexTime = re.compile(r'(\d{2}):(\d{2}):(\d{2})')
rexIP = re.compile(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')
rexMAC = re.compile(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})')
rexURL = re.compile(r'(https?://)?([\w.]+)(/[\w/-]*)?')
print(f'rexEmail: {rexEmail}, type: {type(rexEmail)}')
print("===re.compile正则表达式对象===", end="\n\n")

# todo 1.1 re.match
"""
re.match(pattern, string, flags=0)
从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，返回None
匹配成功的话，match()返回一个匹配对象 匹配对象总是有一个布尔值 True,没匹配则None
re.match
def match(pattern: Pattern[AnyStr],
          string: AnyStr,
          flags: int | RegexFlag = ...) -> Match[AnyStr] | None
pattern 正则表达式字符串或正则表达式对象

正则表达式对象的match方法
def match(self,
          string: AnyStr,
          pos: int = ...,
          endpos: int = ...) -> Match[AnyStr] | None
"""
a = "hellohellohello world"
# 使用if判断, 如果匹配成功, 返回一个Match对象, 进行后续操作
if aRexResult := re.match("hello", a):
    print(aRexResult)
    print(type(aRexResult))
    # 使用Match对象的group()方法, 返回匹配到的字符串
    # group()方法默认返回第0个分组匹配到的字符串, 也就是整个匹配到的字符串
    # group(0)和group()是一样的
    # group(1)返回第一个分组匹配到的字符串, group(2)返回第二个分组匹配到的字符串, 以此类推
    print(aRexResult.group())
    # 使用Match对象的groups()方法, 返回匹配到的字符串组成的元组
    print(aRexResult.groups())
    # 使用Match对象的span()方法, 返回匹配到的字符串的起始位置和结束位置
    print(aRexResult.span())

# 匹配失败, 返回None
print(f're.match("hello", "h") = {re.match("ah", a)}')
# 使用正则表达式对象rexIP, match方法匹配字符串
print(f'{rexIP.match("10.1.1.1、10.1.1.2为本机地址ip地址")}')
print("===re.match从起始位置开始匹配字符串===", end="\n\n")

# todo 1.2 re.search
"""
re.search(pattern, string, flags=0)
扫描整个字符串, 并返回第一个成功的匹配
def search(pattern: Pattern[AnyStr],
           string: AnyStr,
           flags: int | RegexFlag = ...) -> Match[AnyStr] | None

匹配对象的search方法
def search(self,
           string: AnyStr,
           pos: int = ...,
           endpos: int = ...) -> Match[AnyStr] | None           
"""

print(f'a: {a}')
print(f'a中lo: {re.search("lo", a)}')
ipStr = "本机地址ip地址: 10.1.1.1、10.1.1.2"
print(f'{rexIP.search(ipStr)}')
searchIp = re.search(r"(?P<ip1>\d+\.\d+\.\d+\.\d+)、(?P<ip2>\d+\.\d+\.\d+\.\d+)", ipStr)
print(searchIp[1])
print(searchIp.group(2))
print("===re.search搜索整个字符串===", end="\n\n")

# todo 1.3 re.fullmatch
"""
re.fullmatch(pattern, string, flags=0)
如果整个 string 匹配到正则表达式样式，就返回一个相应的 匹配对象 。 否则就返回一个 None 
re.fullmatch
def fullmatch(pattern: Pattern[AnyStr],
              string: AnyStr,
              flags: int | RegexFlag = ...) -> Match[AnyStr] | None
              
匹配对象的fullmatch方法
def fullmatch(self,
             string: AnyStr,
             pos: int = ...,
             endpos: int = ...) -> Match[AnyStr] | None             
"""

print(f'a: {a}')
print(f'lo匹配a: {re.fullmatch("lo", a)}')
patt = re.compile(r"[\w\s]+")
print(f'[\w\s]+匹配a: {re.fullmatch(patt, a)}')
print(f'hellohellohello ss world匹配a: {re.fullmatch("hellohellohello ss world", a)}')
print(rexIP.fullmatch("10.33.45.66"))
print(rexIP.fullmatch("10.33.45.66 10.33.45.66"))
print("===re.fullmatch完全匹配===", end="\n\n")

# todo 1.4 re.split
"""
re.split(pattern, string, maxsplit=0, flags=0)
根据正则表达式pattern, 将string分割成一个列表, 返回分割后的列表
"""

sp1 = re.split(r"\s+", "hello world hello world")
print(sp1, type(sp1))
sp2 = re.split('[a-f]+', '0a3B9', flags=re.I)
print(sp2, type(sp2))
print("===re.split使用正则拆分生成列表===", end="\n\n")

# todo 1.5 re.findall/finditer
"""
re.findall(pattern, string, flags=0)
根据正则表达式pattern, 在string中查找匹配的子串, 返回一个列表

re.finditer(pattern, string, flags=0)
根据正则表达式pattern, 在string中查找匹配的子串, 返回一个迭代器
"""

fa1 = re.findall(r'\bf[a-z]*', 'which foot or hand  fell fastest foot')
print(fa1, type(fa1))
fa2 = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(fa2)

fa3 = re.finditer(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(fa3, type(fa3))
print("===re.findall/finditer查找匹配的子串===", end="\n\n")

# todo 1.6 re.sub/subn
"""
re.sub(pattern, repl, string, count=0, flags=0)
根据正则表达式pattern, 在string中查找匹配的子串, 替换成repl, 返回替换后的字符串
没有找到，则不加改变地返回 string
repl 可以是字符串或函数；如为字符串，则其中任何反斜杠转义序列都会被处理。 
也就是说，\n 会被转换为一个换行符，\r 会被转换为一个回车符，依此类推。
向后引用像是 \6 会用样式中第 6 组所匹配到的子字符串来替换
如果 repl 是一个函数，那它会对每个非重复的 pattern 的情况调用。这个函数只能有一个 匹配对象 参数，并返回一个替换后的字符串

re.subn(pattern, repl, string, count=0, flags=0)
根据正则表达式pattern, 在string中查找匹配的子串, 替换成repl, 返回返回一个元组 (替换后的字符串, 替换次数).
"""

rep1 = re.sub(r'\s+', '|', 'hello world hello world')
print(rep1, type(rep1))
rep2 = re.sub(r'(\w+)=(\d+)', r'\2 \1', 'set width=20 and height=10')
print(rep2)
rep3 = re.sub(r'\d+', lambda x: str(int(x.group())+10), 'set width=20 and height=10')
print(f'rep3:\n{rep3}\n{type(rep3)}')

rep4 = re.subn(r'\s+', '|', 'hello world hello world')
print(rep4, type(rep4))
rep5 = re.subn(r'(\w+)=(\d+)', r'\2 \1', 'set width=20 and height=10')
print(rep5)
print("===re.sub/subn查找替换===", end="\n\n")

# todo 1.7 re.escape
"""
re.escape(pattern)
对字符串中所有的正则表达式特殊字符进行转义, 返回转义后的字符串
在 3.3 版更改: '_' 不再被转义。
在 3.7 版更改: 只有在正则表达式中具有特殊含义的字符才会被转义。 
因此， '!', '"', '%', "'", ',', '/', ':', ';', '<', '=', '>', '@' 和 "`" 将不再会被转义
"""

ec1 = re.escape('https://www.python.org')
print(ec1, type(ec1))
legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
ec2 = re.escape(legal_chars)
print(ec2)
print("===re.escape转义正则表达式特殊字符===", end="\n\n")

# todo 1.8 re.purge
"""
re.purge()
清除正则表达式缓存
"""
re.purge()
