import multiprocessing
import time


def fun1():
    while True:
        print("1--------")
        time.sleep(1)


def fun2():
    while True:
        print("2--------")
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=fun1)
    p2 = multiprocessing.Process(target=fun2)

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
