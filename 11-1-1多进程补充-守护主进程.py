import multiprocessing
import os

# 进程的常用方法
# start()：启动子进程实例（创建子进程）
# join()：主进程会等待子进程执行结束再继续执行（阻塞等待）
# terminate()：不管任务是否完成，立即终止子进程

## 获取当前进程的对象
p = multiprocessing.current_process()
print(p.name)
## 结束进程
os.kill(os.getpid(), 9)
print(p.name)
print(123)
