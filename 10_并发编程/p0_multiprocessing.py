# -*- coding: utf-8 -*-
# @time:         2022/9/9 12:55
# @Author:       Alan
# @File:         p0_multiprocessing.py
# @Software:     PyCharm
# @Description:  multiprocessing 多进程

from multiprocessing import Process, freeze_support

"""
在 multiprocessing 中，通过创建一个 Process 对象然后调用它的 start() 方法来生成进程。

避免共享状态
    应该尽可能避免在进程间传递大量数据，越少越好。
    最好坚持使用队列或者管道进行进程间通信，而不是底层的同步原语。
    
使用 Join 避免僵尸进程
    在 Unix 上，如果一个进程执行完成但是没有被 join，就会变成僵尸进程。 
    一般来说，僵尸进程不会很多，因为每次新启动进程（或者 active_children() 被调用）时，
    所有已执行完成且没有被 join 的进程都会自动被 join，而且对一个执行完的进程调用 
    Process.is_alive 也会 join 这个进程。  
"""


def run_proc(num):
    res = filter(lambda x: x % 2 == 0, range(num))
    sumres = sum(res)
    print(f'子进程运行中，num={num} 和: {sumres}')
    return res



# p2 = Process(target=run_proc, args=(100000,))
# p2.start()
# p2.join()

run_proc(1000)
if __name__ == '__main__':
    freeze_support()
    p = Process(target=run_proc, args=(1000,))
    p1 = Process(target=run_proc, args=(2000,))
    p.start()
    p1.start()
    p.join()
    p1.join()
    print(p)
    print(p1)