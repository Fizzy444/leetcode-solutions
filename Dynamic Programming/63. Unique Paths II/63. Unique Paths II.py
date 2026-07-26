class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0]*m for _ in range(n)]

        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  
        print(dp)
        return dp[-1][-1]