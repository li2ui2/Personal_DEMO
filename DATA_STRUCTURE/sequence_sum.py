def FindContinuousSequence(tsum):
    head = 1
    last = 2
    sum = 3
    r = []
    while last <= (tsum + 1) / 2:
        if sum == tsum:
            r.append(range(head, last + 1))
            last = last + 1
            sum = sum + last
        elif sum < tsum:
            last = last + 1
            sum = sum + last
        else:
            sum = sum - head
            head = head + 1
    return r


if __name__ == '__main__':
    ret = FindContinuousSequence(180)
    print(ret)
