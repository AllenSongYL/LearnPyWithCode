# -*- coding: utf-8 -*-
# @time:         2022/9/9 10:58
# @Author:       Alan
# @File:         p10_threading.py
# @Software:     PyCharm
# @Description:  threading 模块


import threading
import time

"""
threading 模块
    Thread 类，用于表示一个线程对象，通过实例化这个类来创建线程对象
    threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
                    group:  应该为 None；为了日后扩展 ThreadGroup 类实现而保留
                    target: 用于 run() 方法调用的可调用对象
                    name:   线程名称
                    args:   调用目标时传递的参数元组
                    kwargs: 调用目标时传递的关键字参数字典
                    daemon: 设置为 True 表示线程是守护线程，主线程退出时，子线程也会退出;默认为 None，表示继承父线程的守护属性
    
    start() 方法：启动线程
    join() 方法：阻塞当前线程，直到调用此方法的线程终止
    is_alive() 方法：判断线程是否还存活
    getName() 方法：获取线程名称
    setName() 方法：设置线程名称
    isDaemon() 方法：判断线程是否是守护线程
    setDaemon() 方法：设置线程是否是守护线程
    run() 方法：表示线程活动的方法
    ident: 线程标识符
    name: 线程名称
    daemon: 线程是否是守护线程
    native_id: 线程的本地标识符

                  
    Lock 类，用于表示一个锁对象，通过实例化这个类来创建锁对象
    RLock 类，用于表示一个可重入锁对象，通过实例化这个类来创建可重入锁对象
    Condition 类，用于表示一个条件变量对象，通过实例化这个类来创建条件变量对象
    Semaphore 类，用于表示一个信号量对象，通过实例化这个类来创建信号量对象
    Event 类，用于表示一个事件对象，通过实例化这个类来创建事件对象
    Timer 类，用于表示一个定时器对象，通过实例化这个类来创建定时器对象
    Barrier 类，用于表示一个栅栏对象，通过实例化这个类来创建栅栏对象
    BoundedSemaphore 类，用于表示一个有界信号量对象，通过实例化这个类来创建有界信号量对象
    local 类，用于表示一个线程本地对象，通过实例化这个类来创建线程本地对象
    
    enumerate 函数，用于返回当前所有线程的列表
    active_count 函数，用于返回当前活动线程的数量
    current_thread 函数，用于返回当前线程对象
    main_thread 函数，用于返回主线程对象
    settrace 函数，用于设置全局的线程跟踪函数
    setprofile 函数，用于设置全局的线程分析函数
    stack_size 函数，用于设置全局的线程栈大小
     
    
"""


def work():
    print('子线程开始执行')
    time.sleep(2)
    print('子线程执行结束')


start_time = time.time()
t1 = threading.Thread(target=work, name='id1')
t1.start()
t2 = threading.Thread(target=work, name='id2')
t2.start()
t3 = threading.Thread(target=work, name='id3')
t3.start()
t4 = threading.Thread(target=work, name='id4')
t4.start()
print(threading.enumerate())
print(threading.active_count())
t1.join()
t2.join()
t3.join()
t4.join()

end_time = time.time()
print('主线程执行结束，耗时：', end_time - start_time)
