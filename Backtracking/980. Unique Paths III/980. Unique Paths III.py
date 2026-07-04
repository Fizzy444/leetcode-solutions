class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        sx , sy = -1, -1
        total = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] != -1:
                    total += 1
                if grid[i][j] == 1:
                    sx = i
                    sy = j
        
        def dfs(i, j, visited):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == -1:
                return 0
            
            if grid[i][j] == 2:
                if visited == total:
                    return 1
                return 0
            
            temp = grid[i][j]
            grid[i][j] = -1

            path = 0
            path += dfs(i + 1, j, visited + 1)
            path += dfs(i - 1, j, visited + 1)
            path += dfs(i, j + 1, visited + 1)
            path += dfs(i, j - 1, visited + 1)

            grid[i][j] = temp

            return path
        return dfs(sx, sy, 1)