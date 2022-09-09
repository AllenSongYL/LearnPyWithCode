# -*- coding: utf-8 -*-
# @time:         2022/8/30 21:42
# @Author:       Alan
# @File:         interview_questions.py
# @Software:     PyCharm
# @Description:  面试题2 测试
import time


def is_prime(n):
    return False if n < 2 else all(n % number != 0 for number in range(2, n))


def single_thread(p):
    for number in p:
        print(is_prime(number))


def multi_thread(p):
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(3) as executor:
        executor.map(is_prime, p)


def multi_process(p):
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(3) as executor:
        executor.map(is_prime, p)


if __name__ == '__main__':
    PRIMES = [112272535095293] * 20
    start = time.time()
    print(start)
    single_thread(PRIMES)
    end = time.time()
    print('single_thread: ', end - start)
    multi_thread(PRIMES)
    end1 = time.time()
    print('multi_thread: ', end1 - end)
    multi_process(PRIMES)
    end2 = time.time()
    print('multi_process: ', end2 - end1)