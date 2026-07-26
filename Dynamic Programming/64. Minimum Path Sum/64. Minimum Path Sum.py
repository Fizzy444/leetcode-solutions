class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        dp = [[0] * m for _ in range(n)]

        dp[0][0] = grid[0][0]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                up = dp[i-1][j] if i > 0 else float('inf')
                left = dp[i][j-1] if j > 0 else float('inf')
                dp[i][j] = grid[i][j] + min(up, left)
        return dp[-1][-1]