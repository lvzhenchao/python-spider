import random
import time
from multiprocessing import Process

def func(index):
    # 模拟发送邮件的流程，发送需要时间
    time.sleep(random.random())
    print(f'第 {index} 封邮件发送完毕')

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=func, args=(i,))
        p.start()
    print("主进程10封邮件已发送完毕")
    print('')

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