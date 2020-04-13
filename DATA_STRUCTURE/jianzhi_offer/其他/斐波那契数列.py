def Fibonacci(n):
    # write code here
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 1
    b = 0
    ret = None
    if n > 1:
        for i in range(n-1):
            ret = a + b
            b = a
            a = ret
    return ret


if __name__ == '__main__':
    print(Fibonacci(100))
