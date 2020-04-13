def solution(n, s1, s2):
    x, y = 0, 0
    path = []
    for i in range(1, n):
        if x == 0:
            if s1[i] == "x" and s2[i] == "x":
                return -1
            if s1[i] == "." or s2[i] == "x":
                if s2[i] == "x":
                    y += 1

                if s1[i] == "x":
                    x += 1
                    y += 1

        if x == 1:
            if s1[i] == "x" and s2[i] == "x":
                return -1


if __name__ == '__main__':
    n = int(input())
    s1 = str(input())
    s2 = str(input())
    ret = solution(n, s1, s2)
