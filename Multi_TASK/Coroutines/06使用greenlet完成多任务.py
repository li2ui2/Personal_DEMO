from greenlet import greenlet
import time


def task_1():
    while True:
        print("---A---")
        gr2.switch()
        time.sleep(0.5)


def task_2():
    while True:
        print("---B---")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(task_1)
gr2 = greenlet(task_2)
# 切换到gr1中运行
gr1.switch()
