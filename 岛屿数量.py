from typing import List
"""
1、递归
2、DFS（深度优先搜索）
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        递归
        """
        if not grid:
            return 0

        result = 0  # 最终岛屿数量
        m, n = len(grid), len(grid[0])  # 行和列
        for row in range(m):
            for col in range(n): 
                if grid[row][col] == '1':
                    result += 1  # 是1的都算是一个小岛
                    self._numIslands(grid, row, col) # 验证他是不是一个独立的小岛
        return result
 
    def _numIslands(self, grid, x, y): # 递归验证这个数据是不是独立的小岛
        grid[x][y] = '0'
        if 0 < x and grid[x-1][y] == '1':
            self._numIslands(grid, x-1, y)
 
        if 0 < y and grid[x][y-1] == '1':
            self._numIslands(grid, x, y-1)
 
        if y < len(grid[0])-1 and grid[x][y+1] == '1':
            self._numIslands(grid, x, y+1)
 
        if x < len(grid)-1 and grid[x+1][y] == '1':
            self._numIslands(grid, x+1, y)




class Solution2(object):
 
    def numIslands(self, grid):
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > '0':
                    counter += 1
                    self.dfs(grid, i, j)
        return counter
    
    def dfs(self, grid, i, j):
        # 如果越界或到达边线
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0': # 长度大小不一致或者等于0的不符合条件
            return 

        # 对遍历过的点一律设为 0
        grid[i][j] = '0'
        self.dfs(grid, i, j-1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i-1, j)



s = Solution()
s2 = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid2 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(s.numIslands(grid))
print(s2.numIslands(grid2))
