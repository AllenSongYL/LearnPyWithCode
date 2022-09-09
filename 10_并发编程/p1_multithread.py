# -*- coding: utf-8 -*-
# @time:         2022/9/9 10:24
# @Author:       Alan
# @File:         p1_multithread.py
# @Software:     PyCharm
# @Description:


import threading
import time
import p1_threading

# 多线程
# 生产者消费者模型
# 通过 Queue 类来实现线程间的数据通信
import queue


def do_get(url_queue, html_queue):
    while True:
        url = url_queue.get()
        print(url)
        res = p1_threading.get_url(url)
        # url_queue.task_done()
        html_queue.put(res)
        time.sleep(2)


def do_parse(html_queue):
    while True:
        html = html_queue.get()
        # print(html)
        for i in p1_threading.parse(html):
            print(i)
            print("=" * 50)
        time.sleep(3)

star = time.time()
base_url = 'https://www.cnblogs.com/#p'
url_list = [base_url + str(i) for i in range(1, 51)]
q = queue.Queue()
q2 = queue.Queue()
for i in url_list:
    q.put(i)

for _ in range(10):
    t = threading.Thread(target=do_get, args=(q, q2))
    t.start()

for _ in range(10):
    t = threading.Thread(target=do_parse, args=(q2,))
    t.start()

stop = time.time()
print(stop - star)