# -*- coding: utf-8 -*-
"""
通过继承Thread类来创建线程，并引入run方法来运行，
(可以同时有多个方法，但必须要有run方法)，
该方法适用于一个线程里做的事情比较复杂，且分成多个函数去实现。

"""
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        self.login
        self.register
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + " @ " + str(i)  # name属性中保存的是当前线程的名字
            print(msg)
    def login(self):
        pass
    def register(self):
        pass
            

if __name__ == "__main__":
    t = MyThread()
    t.start()  # 只执行run方法中的代码