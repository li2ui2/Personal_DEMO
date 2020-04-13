def qpow(line):
    mod = 1e9+7
    line = line.replace(" ", "")
    n = int(line[0])
    k = int(line[1])
    L = int(line[2])
    R = int(line[3])
    temp = round(R/k - (L+k-1)/k + 1)
    ans = 1
    while n:
        if n & 1:
            ans = (ans * temp) % mod
        temp = (temp * temp) % mod
        n >>= 1
    return int(ans)


if __name__ == '__main__':
    line = str(input())
    ans = qpow(line)
    print(ans)
    n, k, L, R = map(int, input().split())
    num = R - L + 1
    for i in range(L, R+1):
        if i % k:
            num -= 1
    print(num ** n)

