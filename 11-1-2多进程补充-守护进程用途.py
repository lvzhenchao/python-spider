import random
import time
from multiprocessing import Process

def func(index):
    # 模拟发送邮件的流程，发送需要时间
    time.sleep(random.random())
    print(f'第 {index} 封邮件发送完毕')

# if __name__ == '__main__':
#     start = time.time()
#     for i in range(10):
#         p = Process(target=func, args=(i,))
#         p.start()
#     print("1:主进程10封邮件已发送完毕")
#     print('')
#     end = time.time()
#     #查看程序执行时间
#     print('执行时间:%.2f' % (end - start))

## 1、从运行结果看，并没有达到我们的预期，以为父进程和子进程是异步的
## 即使加上休眠，也还是异步的
# 主进程10封邮件已发送完毕
# 第 4 封邮件发送完毕
# 第 8 封邮件发送完毕
# 第 2 封邮件发送完毕
# 第 5 封邮件发送完毕
# 第 0 封邮件发送完毕
# 第 1 封邮件发送完毕
# 第 9 封邮件发送完毕
# 第 6 封邮件发送完毕
# 第 3 封邮件发送完毕
# 第 7 封邮件发送完毕

# if __name__ == '__main__':
#     start = time.time()
#     for i in range(10):
#         p = Process(target=func, args=(i,))
#         p.start()
#         p.join()
#     print("2:主进程10封邮件已发送完毕")
#     print('')
#     end = time.time()
#     #查看程序执行时间
#     print('执行时间:%.2f' % (end - start))

## 2、从运行结果看，join()方法给进程【添加阻塞】，也就是进程运行到【这里就会停滞】
## 从根本上讲，join方法帮我们把异步变成了同步，虽然更加有序，但是并没有给我增加效率
# 第 0 封邮件发送完毕
# 第 1 封邮件发送完毕
# 第 2 封邮件发送完毕
# 第 3 封邮件发送完毕
# 第 4 封邮件发送完毕
# 第 5 封邮件发送完毕
# 第 6 封邮件发送完毕
# 第 7 封邮件发送完毕
# 第 8 封邮件发送完毕
# 第 9 封邮件发送完毕
# 主进程10封邮件已发送完毕

if __name__ == '__main__':
    start = time.time()
    p_list = [] #创建一个空列表
    for i in range(10):
        p = Process(target=func, args=(i,))
        p.start()
        p_list.append(p) # 把启动的进程全部添加进去
    for p in p_list:
        p.join() #添加阻塞
    print("3: 主进程10封邮件已发送完毕")
    print('')
    end = time.time()
    # 查看程序执行时间
    print('执行时间:%.2f' % (end - start))
## 3、将全部进程添加到一个列表中，进程启动的时候仍然是异步，只有结束时所有的阻塞都解除了，主程序才能执行
# 第 0 封邮件发送完毕
# 第 6 封邮件发送完毕
# 第 3 封邮件发送完毕
# 第 9 封邮件发送完毕
# 第 7 封邮件发送完毕
# 第 1 封邮件发送完毕
# 第 4 封邮件发送完毕
# 第 5 封邮件发送完毕
# 第 2 封邮件发送完毕
# 第 8 封邮件发送完毕
# 3: 主进程10封邮件已发送完毕