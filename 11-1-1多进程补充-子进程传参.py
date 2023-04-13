
# 子进程传参；传参的方式有元组和字典两种传参方式
## 元组和字典分别对应Process()的args、kwargs两个参数
### 元组传参：元组的顺序与参数顺序一致
### 字典传参：字典中的key一定要和参数名保持一致

import multiprocessing
import time

def run(name, t):
    for i in range(t):
        print(name, '正在跑-{}'.format(i))
        time.sleep(0.2)

def eat(name, t):
    for i in range(t):
        print(name,t, '吃饭啦-{}'.format(i))
        time.sleep(0.2)

if __name__ == '__main__':
    # 通过元组方式传参(参数位置要对应)
    p1 = multiprocessing.Process(target=run, args=('明_', 5))
    # 通过字典方式传参
    p2 = multiprocessing.Process(target=eat, kwargs={'name': '张', 't': 7})
    p1.start()
    p2.start()
