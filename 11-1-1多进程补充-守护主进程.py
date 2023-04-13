# 若主进程开启了子进程，会等待所有子进程结束之后再结束，即使调用了exit()
import multiprocessing


# 若要结束主进程时也结束子进程，有2种方式
## 1、调用terminate()方法
## 2、设置子进程的daemon属性为True（设置为守护主进程）（守护主进程就是主进程结束时，子进程也被销毁(结束)不再执行）

def task():
    for i in range(10):
        print('执行子进程：', i)

if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=task)
    # sub_process.terminate()
    sub_process.daemon = True
    # sub_process.start()
    print('主进程结束')
    exit()

