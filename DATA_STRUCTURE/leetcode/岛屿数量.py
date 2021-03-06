"""
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。

"""


class Solution:
    def __init__(self):
        self.count = 0

    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.isLand(grid, i, j, rows, cols)
                    self.count += 1

        return self.count

    def isLand(self, grid, i, j, rows, cols):
        grid[i][j] = "0"
        for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            tmp_i = i + x
            tmp_j = j + y
            if 0 <= tmp_i < rows and 0 <= tmp_j < cols and grid[tmp_i][tmp_j] == "1":
                self.isLand(grid, tmp_i, tmp_j, rows, cols)


if __name__ == '__main__':
    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]
    s = Solution()
    print(s.numIslands(grid))

