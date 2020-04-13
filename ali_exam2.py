n, m, q = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
value = []
for i in range(q):
    value.append(list(map(int, input().split())))

ret = []
for i in range(n):
    if A[i][2] - A[i][1] == A[i][1] - A[i][0]:
        ret.append(val for val in A[i])

for i in ret:
    print()

