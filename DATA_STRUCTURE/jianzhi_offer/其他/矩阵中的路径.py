"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如[[a,b,c,e],[s,f,c,s],[a,d,e,e]]矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""


class Solution:
    """
    该方法未通过全部案例
    """
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    if self.find(list(matrix), rows, cols, path[1:], i, j):
                        return True
        return False

    def find(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i*cols+j] = '0'  # 表示该位置已经走过

        if j+1 < cols and matrix[i*cols+j+1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j+1)
        elif j-1 >= 0 and  matrix[i*cols+j-1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j-1)
        elif i+1 < rows and matrix[(i+1)*cols+j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i+1, j)
        elif i-1 >= 0 and matrix[(i-1)*cols+j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i-1, j)
        else:
            return False

# class Solution:
#     """
#     该方法通过全部样例
#     """
#     def hasPath(self, matrix, rows, cols, path):
#         # write code here
#         for i in range(0, rows):
#             for j in range(0, cols):
#                 flags = [0] * (rows * cols)
#                 if self.isPath(matrix, i, j, rows, cols, path, flags, 0):
#                     return True
#         return False
#
#     def isPath(self, matrix, row, col, rows, cols, path, flags, index):
#         if index == len(path):
#             return True
#         if row >= rows or col >= cols or row < 0 or col < 0 or flags[row*cols + col]:
#             return False
#         if matrix[row*cols + col] == path[index]:
#             flags[row*cols + col] = 1
#             return self.isPath(matrix, row + 1, col, rows, cols, path, flags, index + 1) or \
#                    self.isPath(matrix, row - 1, col, rows, cols, path, flags, index + 1) or \
#                    self.isPath(matrix, row, col + 1, rows, cols, path, flags, index + 1) or \
#                    self.isPath(matrix, row, col - 1, rows, cols, path, flags, index + 1)
#         else:
#             return False


if __name__ == '__main__':
    s = Solution()
    rows = 3
    cols = 4
    matrix = "ABCESFCSADEE"
    # matrix = ['a', 'b', 'c', 'e',
    #           's', 'f', 'c', 's',
    #           'a', 'd', 'e', 'e']
    # path = ['b', 'c', 'c', 'e', 'd']
    # path2 = ['a', 'b', 'c', 'b']
    path = "SEE"

    print(s.hasPath(matrix, rows, cols, path))
