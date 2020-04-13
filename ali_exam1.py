# list(map(int, input().split()))
n = int(input())
a = []
for i in range(3):
    a.append(list(map(int, input().split())))
dp = [[0 for _ in range(n)] for _ in range(3)]

if len(a) == 0:
    print(0)

INF = 0x7fffffff
for j in range(1, n):
    for i in range(3):
        dp[i][j] = INF
        for k in range(3):
            dp[i][j] = min(dp[k][j-1] + abs(a[k][j-1] - a[i][j]), dp[i][j])
ans = min(dp[0][n-1], dp[1][n-1], dp[2][n-1])
print(ans)
