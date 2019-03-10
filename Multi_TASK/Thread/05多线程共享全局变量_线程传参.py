# -*- coding: utf-8 -*-

import threading
import time


def fun1(temp):
    temp.append(33)
    print("-----in test1 g_nums = %s-----" % str(temp))
    
    
def fun2(temp):
    print("-----in test2 g_nums = %s-----" % str(temp))


g_nums = [11, 22]


def main():
    # target指定将来这个线程去哪个函数执行代码
    # args指定将来调用函数的时候，传递什么数据过去，该参数需要是一个元组
    t1 = threading.Thread(target=fun1, args=(g_nums,))
    t2 = threading.Thread(target=fun2, args=(g_nums,))
    
    t1.start()
    time.sleep(1)
    
    t2.start()
    time.sleep(1)
    
    print("-----in main Thread g_nums = %s-----" % str(g_nums))


if __name__ == "__main__":
    main()

