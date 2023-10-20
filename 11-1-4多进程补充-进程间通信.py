
# 每个进程都在自己的独立空间内，互不干扰，但有些情况下想要实现进程间通信也是可以的，我们可以使用Queue、Pipes等工具
import os
import random
import time
from multiprocessing import Process, Queue


def put_data(q):
    print("Process put_data id:{}".format(os.getpid()))
    for data in ["云天河", "韩菱纱", "柳梦璃", "慕容紫英"]:
        print("put data {}".format(data))
        q.put(data)
        time.sleep(random.random())

def get_data(q):
    print("Process get_data id: {}".format(os.getpid()))
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    start = time.time()

    queue = Queue()
    p_put = Process(target=put_data, args=(queue,))
    p_get = Process(target=get_data, args=(queue,))

    p_put.start()
    p_get.start()

    p_put.join()
    p_get.terminate()

    end = time.time()
    # 查看程序执行时间
    print('执行时间:%.2f' % (end - start))
