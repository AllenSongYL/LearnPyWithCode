# -*- coding: utf-8 -*-
# @time:         2022/9/9 12:29
# @Author:       Alan
# @File:         p11_ThreadPoolExecutor.py
# @Software:     PyCharm
# @Description:  ThreadPoolExecutor

import time
from concurrent.futures import ThreadPoolExecutor, as_completed

"""
ThreadPoolExecutor 是一个线程池，它可以用来执行那些耗时的函数调用，从而不会阻塞主线程的执行。
ThreadPoolExecutor 类的构造方法接收两个参数，第一个是最大线程数，第二个是线程名的前缀。

submit() 方法用来提交一个可调用对象到线程池中，它会返回一个 Future 对象。
Future 对象代表将来执行或没有执行的任务的结果。可以通过 Future 对象的 done() 方法来判断任务是否完成。
通过 Future 对象的 result() 方法可以获取任务的返回值，如果任务没有完成，则 result() 方法会一直阻塞直到任务完成。

map() 方法用来提交一组可调用对象到线程池中，它会返回一个迭代器，可以通过迭代器来获取每个任务的返回值。
def map(self,
        fn: (...) -> _T,
        *iterables: Iterable,
        timeout: float | None = ...,
        chunksize: int = ...) -> Iterator[_T]
        
        
as_completed() 方法会在任务完成后返回一个 Future 对象，可以通过迭代器来获取每个任务的返回值。
def as_completed(fs: Iterable[Future[_T]]) -> Iterator[Future[_T]]
                
"""

# with ThreadPoolExecutor() as pool:
# res = pool.map(lambda x: x * x, range(10))
# print(list(res))

# with ThreadPoolExecutor() as pool:
#     fut = [pool.submit(lambda x: x * x, i) for i in range(10)]
#
#     # 遍历方法1
#     for i in fut:
#         print(i.result())
#
#     # 遍历方法2
#     for fu in as_completed(fut):
#         print(fu.result())

#
pool = ThreadPoolExecutor(max_workers=10, thread_name_prefix='test')

