from multiprocessing import Pool
import os
import time
import random


def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print("执行完毕，耗时为%0.2f" % (t_stop-t_start))


def main():
    po = Pool(3)  # 定义一个进程池，最大进程数3
    # po.map(worker, range(10))
    # 以下for循环等同于执行po.map函数
    for i in range(10):
        # Pool().apply_async(要调用的目标, (传递给目标的参数元组,))
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker, (i,))

    print("-----start-----")
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成(主进程阻塞等待子进程的退出)，必须放在close语句之后
    print("-----end-----")


if __name__ == "__main__":
    main()
