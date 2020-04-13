import collections


def find_num(line1, line2):
    n = int(line1[0])
    x = int(line1[2])
    A = line2.replace(" ", "")
    if line2 is None or n == 0:
        return 0
    orA = []
    ret = 0
    count = collections.Counter(A)
    for i in range(n):
        orA.append(str(int(A[i]) | x))
    for i in range(n):
        if A[i] != orA[i]:
            count[orA[i]] += 1
    for key in count:
        temp = count[key]
        ret = max(ret, temp)
    return ret


if __name__ == '__main__':
    line1 = str(input())
    line2 = str(input())
    ret = find_num(line1, line2)
    print(ret)

