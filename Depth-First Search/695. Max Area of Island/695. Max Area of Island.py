class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        max_area = 0

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0

            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)

            return area
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 1:
                    max_area = max(max_area, dfs(x, y))
        return max_area