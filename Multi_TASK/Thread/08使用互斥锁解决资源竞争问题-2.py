"""共享全局变量可能产生资源竞争问题"""
import threading
import time

# 定义一个全局变量
g_num = 0


def fun1(num):
    global g_num
    # 上锁，如果之前没有被上锁，那么此时上锁成功
    # 如果上锁之前 已经被上锁了，那么此时会堵塞在这里，直到这个锁被解开位置
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("-----in test1 g_num = %d-----" % g_num)


def fun2(num):
    global g_num

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("-----in test2 g_num = %d-----" % g_num)


# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=fun1, args=(1000000,))
    t2 = threading.Thread(target=fun2, args=(1000000,))

    t1.start()
    t2.start()
    # 等待上面的2个线程执行完毕
    time.sleep(5)
    print("-----in main Thread g_num = %d-----" % g_num)


if __name__ == "__main__":
    main()

