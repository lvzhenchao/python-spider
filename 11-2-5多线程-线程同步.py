
# 一般主线程要等子线程的任务结束之后才会结束，即时调用了exit()

# 可以把子线程设置为守护主线程，这样一旦主线程要结束，子线程也会立即结束
# 将子线程设置为主线程的方法有三种

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
    print('main：主线程为', threading.current_thread())

    # 设置为守护主线程
    ## 方法1创建线程时指定daemon参数
    # run_thread = threading.Thread(target=run, daemon=True)
    # eat_thread = threading.Thread(target=eat, daemon=True)
    # print('main：主线程为', threading.current_thread())

    ## 方法2设置setDaemon()方法:设置为True时，就相当于是守护线程，该线程进入后台工作，可以把其想为不是很重要的线程
    # run_thread.setDaemon(True)
    # eat_thread.setDaemon(True)

    ## 方法3设置daemon属性
    # run_thread.daemon = True
    # eat_thread.daemon = True

    # 2、开启线程
    run_thread.start()
    eat_thread.start()