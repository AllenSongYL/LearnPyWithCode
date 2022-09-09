# -*- coding: utf-8 -*-
# @time:         2022/9/9 8:37
# @Author:       Alan
# @File:         p0_requests.py
# @Software:     PyCharm
# @Description:  requests 库

import requests

"""
requests方法
get(url, params=None, **kwargs)
post(url, data=None, json=None, **kwargs)

put(url, data=None, **kwargs)
patch(url, data=None, **kwargs)
delete(url, **kwargs)
head(url, **kwargs)
options(url, **kwargs)

request(method, url, **kwargs)

返回值：Response对象
========================================================================================================

Response对象属性
r.status_code               状态码
r.ok                        检查 "status_code" 的值，如果小于400，则返回 True，如果不小于 400，则返回 False
r.reason                    状态码的原因短语，比如 "Not Found" 或 "OK"
    
r.headers                   返回响应头，字典格式
r.url                       返回响应的 URL
r.history                   返回包含请求历史的响应对象列表（url）
r.cookies                   返回一个 CookieJar 对象，包含了从服务器发回的 cookie
r.elapsed                   返回一个 timedelta 对象，表示请求的时间
r.elapsed.microseconds      返回请求的时间，单位为微秒
r.elapsed.total_seconds()   返回请求的时间，单位为秒
is_permanent_redirect       如果响应是永久重定向的 url，则返回 True，否则返回 False
is_redirect                 如果响应被重定向，则返回 True，否则返回 False

r.raw                       原始响应内容    
r.text                      返回响应的内容，unicode 类型数据
r.content                   返回响应的内容，以字节为单位
r.encoding                  解码 r.text 的编码方式
r.apparent_encoding         从内容中分析出的响应内容编码方式

========================================================================================================

Response对象方法          
r.json()                返回结果的 JSON 对象 (结果需要以 JSON 格式编写的，否则会引发错误)
r.raise_for_status()    如果发生错误，方法返回一个 HTTPError 对象
r.iter_content(chunk_size=1, decode_unicode=False)
                        返回一个迭代器，每次迭代返回 chunk_size 个字节的内容
r.iter_lines(chunk_size=512, decode_unicode=None, delimiter=None)
                        返回一个迭代器，每次迭代返回一行内容
r.close()               关闭与服务器的连接

========================================================================================================
"""

req = requests.get('https://www.cnblogs.com/#p1')
print(f"返回对象: {req} \n"
      f"类型: {type(req)}\n"
      f"请求头: {req.headers}\n"
      f"状态码: {req.status_code}\n"
      f"编码: {req.encoding}\n"
      # f"响应内容: {req.text}\n"
      f"响应内容: {req.ok}\n"
      f"响应url: {req.url}\n"
      f"历史: {req.history}\n"
      f"响应状态的描述: {req.reason}\n"
      f"编码方式: {req.apparent_encoding}\n"
      f"响应速度: {req.elapsed}\n"
      f"永久重定向: {req.is_permanent_redirect}\n"
      f"重定向: {req.is_redirect}\n"
      f"cookies: {req.cookies}\n"
      f"raw: {req.raw}\n"
      f"content: {req.iter_content(50)}\n"
      f"lines: {req.iter_lines(chunk_size=2)}\n"
      f"响应的内容: {req.text}\n")

# print(req.status_code)
# print(req.headers)
# print(req.text)