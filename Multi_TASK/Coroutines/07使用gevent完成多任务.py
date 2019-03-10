import gevent
import time
from gevent import monkey


# 有耗时操作时，需要加入第8行代码，可以实现不改变代码中原来设定的延时方式
# 以下语句实现功能:将程序中用到的耗时操作的代码,换为gevent自己实现的模块
monkey.patch_all()


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)


# gevent.spawn相当于创建greenlet对象
# g1 = gevent.spawn(f1, 5)
# g2 = gevent.spawn(f2, 5)
# g3 = gevent.spawn(f3, 5)
# g1.join()  # 遇到延时就等待
# g2.join()
# g3.join()


gevent.joinall([
    gevent.spawn(f1, 5),
    gevent.spawn(f2, 5),
    gevent.spawn(f3, 5)
])
