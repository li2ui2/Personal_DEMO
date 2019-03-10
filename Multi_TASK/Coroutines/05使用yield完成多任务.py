import time


def task1():
    while True:
        print("----1----")
        time.sleep(0.1)
        yield


def task2():
    while True:
        print("----2----")
        time.sleep(0.1)
        yield


def main():
    t1 = task1()
    t2 = task2()
    # 实现并发操作，即协程，其占用资源比线程更少
    # 先让t1运行一会，当t1中遇到yield的时候，再返回到25行，然后
    # 执行t2，当它遇到yield的时候，再次切换到t1中
    # 这样t1/t2/t1/t2的交替运行，最终实现了多任务...协程
    while True:
        next(t1)
        next(t2)


if __name__ == "__main__":
    main()
