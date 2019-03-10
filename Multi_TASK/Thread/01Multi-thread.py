import time
import threading


def sing():
    """唱歌 5秒钟"""
    for i in range(5):
        print("------正在唱歌--------")
        time.sleep(1)


def dance():z
    """跳舞 5秒钟"""
    for i in range(5):
        print("------正在跳舞--------")
        time.sleep(1)


def main():
    # 当调用Thread的时候，不会创建线程
    # 当调用Thread创建出来的实例对象的start方法的时候，
    # 才会创建线程以及让这个线程开始运行
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()  # 启动线程，即让线程开始运行
    t2.start()


if __name__ == "__main__":
    main()
