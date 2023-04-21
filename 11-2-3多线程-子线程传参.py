
# 如果子线程执行的任务需要参数，可以通过元组和字典两种方法指定参数
#
# args参数对应的是元组，元组里的元素位置要和被调用的方法里参数顺序一致
# kwargs参数对应的是字典，字典里的键要和被调用的方法里的参数名一致

import threading
import time

def run(name, t):
    print(name, t,'run: 当前的线程为{}'.format(threading.current_thread()))
    for i in range(5):
        print('跑：{}'.format(i))
        time.sleep(1)

def eat(name, t):
    print(name, t,'run：当前的线程为{}'.format(threading.current_thread()))
    for i in range(5):
        print('吃饭啦: {}'.format(i))
        time.sleep(1)

if __name__ == '__main__':
    # 1、创建线程
    run_thread = threading.Thread(target = run, args=('小明', 5))
    eat_thread = threading.Thread(target = eat, kwargs={'name': '小红', 't': 6})
    print('main：主线程为', threading.current_thread())


    # 2、开启线程
    run_thread.start()
    eat_thread.start()