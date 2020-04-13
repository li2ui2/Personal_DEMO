def setZeroes(matrix):
    n = len(matrix)
    if n == 0:
        return []
    m = len(matrix[0])
    for i, li in enumerate(matrix):
        for j in range(len(li)):
            if li[j] == 0:
                matrix[i] = [0 for _ in range(m)]
                for i in range(n):
                    matrix[i][j] = 0
    return matrix


if __name__ == '__main__':
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(setZeroes(matrix))
