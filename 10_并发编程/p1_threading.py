# -*- coding: utf-8 -*-
# @time:         2022/9/9 7:31
# @Author:       Alan
# @File:         p1_threading.py
# @Software:     PyCharm
# @Description:  多线程 并发编程
# import io
# import sys
import threading
import time
import requests
from bs4 import BeautifulSoup

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def say_after(delay, what):
    time.sleep(delay)
    print(what)


# 创建一个线程
# t1 = threading.Thread(target=say_after, args=(2, 'hello'))
# t2 = threading.Thread(target=say_after, args=(2, 'world'))
# 启动线程
# t1.start()
# t2.start()
# 等待线程结束
# t1.join()
# t2.join()
# print(f'{"finish".center(50, "=")}')


# 通过继承 Thread 类来创建自定义的线程类
class MyThread(threading.Thread):
    def __init__(self, delay, what):
        super().__init__()
        self.delay = delay
        self.what = what

    def run(self):
        time.sleep(self.delay)
        print(self.what)


# t3 = MyThread(2, 'hello')
# t4 = MyThread(2, 'world')
# t3.start()
# t4.start()
# t3.join()
# t4.join()
# print(f'{"finish".center(50, "=")}')

# 多线程数据通信
# 通过 Queue 类来实现线程间的数据通信
import queue

# 创建一个队列
# q = queue.Queue()
# 向队列中添加数据，如果队列已满，会阻塞
# q.put(item='hello')
# 从队列中获取数据，如果队列为空，阻塞等待
# item = q.get()
# print(item)  # hello
# 查看队列中的数据个数
# print(q.qsize())  # 0
# 查看队列是否为空
# print(q.empty())  # True
# 查看队列是否已满
# print(q.full())  # False


# 测试
base_url = 'https://www.cnblogs.com/#p'
url_list = [base_url + str(i) for i in range(1, 51)]
print(url_list)

# q = queue.Queue()
# 将url列表添加到队列中
# q.put(url_list)


# 定义一个get请求函数
def get_url(url):
    # 发送请求
    response = requests.get(url)
    # print(f"url: {response.url}\n状态码: {response.status_code}\n内容大小: {len(response.text)}")
    return response.text


# 定义一个解析函数
def parse(html):
    sp = BeautifulSoup(html, 'html.parser')
    links = sp.find_all('a', class_='post-item-title')
    return [(i["href"], i.get_text()) for i in links]


# star = time.time()
# # 创建多个线程
# for i in range(50):
#     # t = threading.Thread(target=get_url, args=(url_list[i],))
#     # t.start()
#     # # 阻塞等待队列中的任务完成
#     # t.join()
#     print(url_list[i])
#     for j in parse(get_url(url_list[i])):
#         print(j)
# end = time.time()
# print(f'耗时: {end - star}')
# print(f'{"finish".center(50, "=")}')
