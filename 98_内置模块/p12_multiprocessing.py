# -*- coding: utf-8 -*-
# @time:         2022/9/9 13:55
# @Author:       Alan
# @File:         p12_multiprocessing.py
# @Software:     PyCharm
# @Description:  multiprocessing模块

"""
multiprocessing模块
multiprocessing模块提供了一个Process类来代表一个进程对象

Pool 进程池
    Pool 对象提供了批量创建进程的方法，可以使用进程池的方式批量创建进程。
    Pool 对象的方法：
        apply(func[, args[, kwds]])：调用func，args和kwds是传递给func的参数,返回结果前阻塞
        apply_async(func[, args[, kwds[, callback]]])：使用非阻塞方式调用func，args和kwds是传递给func的参数。
        close()：关闭进程池，使其不在接受新的任务。
        join()：主进程阻塞，等待子进程的退出， join方法要在close或terminate之后使用。
        map(func, iterable[, chunksize])：使用阻塞方式调用func，iterable是一个可迭代对象，chunksize是分块的大小。
        map_async(func, iterable[, chunksize[, callback]])：使用非阻塞方式调用func，iterable是一个可迭代对象，chunksize是分块的大小。
        terminate()：不管任务是否完成，立即终止。
        is_alive()：判断进程池是否还在运行。
        imap(func, iterable[, chunksize])：map() 的延迟执行版本。
        imap_unordered(func, iterable[, chunksize])：imap() 的无序版本。
        get()：获取返回值。
        wait()：等待所有子进程结束。
        ready()：判断是否所有子进程都已经结束。
        successful()：判断是否所有子进程都执行成功。
"""

from multiprocessing import Pool, TimeoutError
import time
import os


def f(x):
    return x * x


if __name__ == '__main__':
    # start 4 worker processes
    print(os.cpu_count())
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # print same numbers in arbitrary order
        for i in pool.imap_unordered(f, range(10)):
            print(i)

        # evaluate "f(20)" asynchronously
        res = pool.apply_async(f, (20,))  # runs in *only* one process
        print(res.get(timeout=1))  # prints "400"

        # evaluate "os.getpid()" asynchronously
        res = pool.apply_async(os.getpid, ())  # runs in *only* one process
        print(res.get(timeout=1))  # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(os.getpid, ()) for _ in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        # make a single worker sleep for 10 secs
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")
