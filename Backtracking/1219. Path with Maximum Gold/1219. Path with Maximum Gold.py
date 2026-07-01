class Solution:
    def dfs(self, grid, i, j, n, m):
        if i < 0 or i >= n or  j < 0 or j >= m or grid[i][j] == 0:
            return 0
        
        curr = grid[i][j]
        grid[i][j] = 0

        tempmax = max(
            self.dfs(grid, i + 1, j, n, m),
            self.dfs(grid, i - 1, j, n, m),
            self.dfs(grid, i, j + 1, n, m),
            self.dfs(grid, i, j - 1, n, m)
        )

        grid[i][j] = curr
        return tempmax + curr

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        maxGold = 0
        for i in range(n):
            for j in range(m):
                maxGold = max(maxGold, self.dfs(grid, i, j, n, m))
        return maxGold