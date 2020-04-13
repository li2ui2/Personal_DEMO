class Solution:
    def __init__(self):
        self.count = 0
        self.max_Area = 0
        self.temp = 0
        self.directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                self.temp = 0
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, rows, cols)
                    self.temp += 1
                    self.max_Area = max(self.max_Area, self.temp)
                    self.count += 1
        return self.max_Area

    def dfs(self, grid, i, j, rows, cols):
        grid[i][j] = 0  # 标记
        for x, y in self.directions:
            new_i = i + x
            new_j = j + y
            if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == 1:
                self.temp += 1
                self.dfs(grid, new_i, new_j, rows, cols)


if __name__ == '__main__':
    grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    s = Solution()
    print(s.maxAreaOfIsland(grid))
