def max_score(n, m, a, b):
    if m > n or n <= 0:
        return 0
    ans = 0
    a.sort()
    b = b.sort()
    alen = len(a)
    for i in range(m):
        ans += a[-1]
        a.pop(-1)
        alen -= 1
        for j in range(alen):
            a[j] -= b[j]
        a.sort()
    return ans


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max_score(n, m, a, b))
