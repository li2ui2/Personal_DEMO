def _sqrt(a):
    x1 = a
    x2 = a/2
    while abs(x1-x2) > 0.00000001:
        x1 = x2
        x2 = (x1+a/x1)/2
    return x1


if __name__ == '__main__':
    print(int(_sqrt(25)))
