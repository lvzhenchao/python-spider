
# 网络爬虫是一种IO密集型程序，涉及了很多【网络IO】以及本地【磁盘IO】操作，会消耗大量的时间，降低程序的执行效率
# 多线程可以提升IO密集程序的执行效率

# 两个多线程模块：_thread和threading;
## _thread模块偏底层，功能有限
## threading是_thread的超集，包含了_thread模块的所有方法，还提供了一些其他方法
###- threading.currentThread() 返回当前的线程变量
###- threading.enumerate() 返回一个所有正在运行的线程的列表
###- threading.activeCount() 返回正在运行的线程数量

# 线程的具体使用方法
from threading import Thread

def demo(num):
    print(num, "test function")

## 1、 线程创建、启动、回收
t = Thread(demo(100)) # 创建线程对象
t.start() # 创建并启动线程
t.join()  # 阻塞等待回收线程

## 2、 创建多线程的具体流程
t_list = []

for i in range(5):
    t = Thread(demo(i))
    t_list.append(t)
    t.start()

for t in t_list:
    t.join()



## 3、线程同步问题：即多个线程不能操作同一个数据，会造成数据的不确定性；通过threading 模块的 Lock 对象能够保证数据的正确性
from threading import Lock
# lock = Lock()
# # 获取锁
# lock.acquire()
# wirter.writerows("线程锁问题解决")
# # 释放锁
# lock.release()