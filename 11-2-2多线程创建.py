
# 线程是CPU调度的基本单位，线程不能独立存在，依附于进程

# 特点：
## 线程执行是无序的，由CPU调度
## 进程不能共享全局变量，线程是共享全局变量的，但要注意资源竞争问题
## 主线程会等待子线程结束才能结束
## 只要有一个线程不是守护主线程，主线程都会等待该子线程执行完之后再结束，期间其他守护主线程都可以继续执行

import threading
import time

def run():
    print('run: 当前的线程为{}'.format(threading.current_thread()))
    for i in range(5):
        print('跑：{}'.format(i))
        time.sleep(1)

def eat():
    print('run：当前的线程为{}'.format(threading.current_thread()))
    for i in range(5):
        print('吃饭啦: {}'.format(i))
        time.sleep(1)

if __name__ == '__main__':
    # 1、创建线程
    run_thread = threading.Thread(target = run)
    eat_thread = threading.Thread(target = eat)
    print('man：主线程为', threading.current_thread())

    # 2、开启线程
    run_thread.start()
    eat_thread.start()