class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return ret
    
    def turn(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        new_matrix = []
        for i in range(m):
            new_matrix2 = []
            for j in range(n):
                new_matrix2.append(matrix[j][i])
            new_matrix.append(new_matrix2)
        new_matrix.reverse()
        return new_matrix
