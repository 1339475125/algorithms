from typing import List
"""
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 
1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_size, col_size = len(nums), len(nums[0])
        max_data = 0
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == 1:
                    res = 0
                    data = self.get_max_size(grid, i, j, res)
                    max_data = max(max_data, data)
        return max_data

    def get_max_size(self, grid, x, y, d):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y]==0:
            return d
        grid[x][y] = 0
        d = d + 1
        n = self.get_max_size(grid, x-1, y, d)
        m = self.get_max_size(grid, x+1, y, n)
        u = self.get_max_size(grid, x, y-1, m)
        v = self.get_max_size(grid, x, y+1, u)
        return v


nums = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]

s = Solution()
print(s.maxAreaOfIsland(nums))
