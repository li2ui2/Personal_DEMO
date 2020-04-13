def find_max_nl(n, l):
    left = 1
    right = 2
    sum = 3
    lll = None
    ret = []
    while right <= (n + 1) / 2:
        if sum == n:
            temp = list(range(left, right+1))
            temp_len = len(temp)
            if lll is None:
                lll = temp_len
            if l <= temp_len < lll:
                ret = temp
                lll = temp_len
            right += 1
            sum += right
        if sum < n:
            right += 1
            sum += right
        else:
            sum -= left
            left += 1
    return ret


if __name__ == '__main__':
    n, l = map(int, input().split())
    a = input()
    ret = find_max_nl(n, l)
    for i, val in enumerate(ret):
        if i == len(ret) - 1:
            print(val, end="")
        else:
            print(val, end=" ")

