
# 多任务：同一时间，多个任务同时执行
# 并发：多个任务交替执行
# 并行：多个任务真正同时执行
## 进程可以使用多核；线程不能使用多核，但可以使用并发实现多任务；
## 进程资源开销大，线程资源开销小
## 进程稳定性大，线程稳定性小

## 计算密集型：使用多进程更好
## io密集型：使用多线程更好

import multiprocessing
import os
import time

def run():
    print("run 当前进程:{}，父进程:{}".format(os.getpid(), os.getppid()))
    for i in range(0, 5):
        print('正在跑第{}次', format(i))
        time.sleep(0.2)

def eat():
    print("eat 当前进程:{}，父进程:{}".format(os.getpid(), os.getppid()))
    for i in range(0, 5):
        print('吃饭啦---{}次', format(i))
        time.sleep(0.2)

if __name__ == '__main__':
    print('主进程：' + str(os.getpid()))
    run_process = multiprocessing.Process(target=run)
    eat_process = multiprocessing.Process(target=eat)
    run_process.start()
    eat_process.start()
