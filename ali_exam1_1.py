import os

(m, n, num) = list(map(int,input().split(" ")))


def judege_unknowed(a):
    count = 0
    for index,data in enumerate(a):
        if data==0:
            continue
        else:
            count+=1
        if count == 1:
            left_index,left = index+1,data
        elif count == 2:
            sub_value = (data-left)/(index+1-left_index)
            return True, left_index, left, sub_value
    return False, 0, 0, 0


def cal_val(l, col):
    if col==l[1]:
        return l[2]
    else:
        return l[2]+l[3]*(col-l[1])
matrix = []
for i in range(m):
    matrix.append(judege_unknowed(list(map(int,input().split(" ")))))

for i in range(num):
    row,col = list(map(int,input().split(" ")))
    if (matrix[row-1][0]):
        print(int(cal_val(matrix[row-1],col)))
    else:
        print("Unknown")
