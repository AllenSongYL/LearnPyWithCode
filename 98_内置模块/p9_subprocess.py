# -*- coding: utf-8 -*-
# @time:         2022/9/6 10:37
# @Author:       Alan
# @File:         p9_subprocess.py
# @Software:     PyCharm
# @Description:  subprocess

"""
subprocess 模块允许你生成新的进程，连接它们的输入、输出、错误管道，并且获取它们的返回码。
推荐的调用子进程的方式是在任何它支持的用例中使用 run() 函数。对于更进阶的用例，也可以使用底层的 Popen 接口。
"""

import subprocess


# todo 1.0 subprocess.run
"""
运行被 arg 描述的指令. 等待指令完成, 然后返回一个 CompletedProcess 实例
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, 
shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, 
env=None, universal_newlines=None, **other_popen_kwargs)

    args: 要执行的命令，可以是字符串或者序列类型。
    stdin: 传递给子进程的标准输入。默认为None，表示使用父进程的标准输入。
    input: input参数将被传递给 Popen.communicate() 以及子进程的 stdin;必须是一个字节序列
    stdout: 传递给子进程的标准输出。默认为None，表示使用父进程的标准输出。
    stderr: 传递给子进程的标准错误。默认为None，表示使用父进程的标准错误。
    capture_output: 如果为True，stdout和stderr将被捕获。默认为False。
    shell: 如果为True，表示通过shell执行。默认为False。
    cwd: 子进程的当前目录。默认为None，表示使用父进程的当前目录。
    timeout: 超时时间，单位为秒。默认为None，表示不设置超时时间。
    check: 如果为True，表示检查子进程的返回码。如果返回码不为0，则抛出CalledProcessError异常。默认为False。
    encoding: 子进程的输出编码。默认为None，表示不编码。
    errors: 子进程的输出编码错误处理方式。默认为None，表示使用默认的错误处理方式。
    text: 如果为True，表示以文本模式打开文件。默认为None，表示不以文本模式打开文件。
    env: 子进程的环境变量。默认为None，表示使用父进程的环境变量。
    universal_newlines: 如果为True，表示使用通用换行模式（universal newlines mode）。默认为None，表示不使用通用换行模式。
    other_popen_kwargs: 其他参数，将被传递给 Popen 构造函数。
    
subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)
"""


p = subprocess.run('dir', shell=True, capture_output=True)
print(p, '\n', type(p))


# todo 2.0 subprocess.Popen
"""
此模块的底层的进程创建与管理由 Popen 类处理。它提供了很大的灵活性，因此开发者能够处理未被便利函数覆盖的不常见用例。
在一个新的进程中执行子程序。 
class subprocess.Popen(args, bufsize=- 1, executable=None, stdin=None, 
stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, 
cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0, 
restore_signals=True, start_new_session=False, pass_fds=(), *, 
group=None, extra_groups=None, user=None, umask=- 1, encoding=None, errors=None, text=None, pipesize=- 1)
"""

subprocess.Popen(['ping', '127.0.0.1'], shell=True)
