# -*- coding: utf-8 -*-
# @time:         2022/9/8 19:45
# @Author:       Alan
# @File:         p1_asynico.py
# @Software:     PyCharm
# @Description:  Python异步编程

"""
asyncio.run() 函数是 Python 3.7 引入的新函数，用于简化事件循环的创建和关闭。
它的作用是：创建一个事件循环，运行协程，然后关闭事件循环。

要真正运行一个协程，asyncio 提供了三种主要机制:
asyncio.run() 函数用来运行最高层级的入口点 "main()" 函数

asyncio.wait() 函数用来等待一组协程对象运行结束

asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程。
"""

import asyncio
import time


# 简单地调用一个协程并不会使其被调度执行
# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')
#
#
# asyncio.run(main())


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
#
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#
#     print(f"finished at {time.strftime('%X')}")
#
#
# asyncio.run(main())


async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))

    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should takearound 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())