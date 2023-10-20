import threading

# 如果多个线程同时操作同一个全局变量，可能会造成资源竞争的问题，导致数据出错，解决资源竞争问题的方法有两个
## 线程同步：调用join()方法，等当前线程结束才会继续执行，但是这样失去了多线程的优势
## 线程异步：互斥锁，保护共享数据，保证同一时刻只有一个线程可以访问公共资源，谁抢到锁谁就能访问资源，访问完之后释放资源

### 互斥锁3步骤：创建锁、上锁、解锁
# 创建锁
# mutex = threading.Lock()
# 上锁
# mutex.acquire()
# 这个部分的代码会被锁定，其他线程不能访问，直到释放锁
# 释放锁
# mutex.release()

# 参考：https://binglengdexiwang.blog.csdn.net/article/details/107836757

g_num = 0
# 第1步：创建锁
mutex = threading.Lock()

def task1():
    global g_num
    # 第2步：上锁
    mutex.acquire()
    try:
        for i in range(1000000):
            g_num += 1
    finally:
        # 第3步：解锁
        mutex.release()
    print("task1:",g_num)

def task2():
    global g_num
    mutex.acquire()
    try:
        for i in range(1000000):
            g_num += 1
    finally:
        mutex.release()
    print("task2:",g_num)

if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
