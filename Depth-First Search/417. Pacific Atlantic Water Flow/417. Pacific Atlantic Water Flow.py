class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, vis):
            vis.add((i, j))
            for x, y in dir:
                dx,dy = x + i, y + j
                if 0 <= dx < n and 0 <= dy < m:
                    if (dx, dy) not in vis and heights[dx][dy] >= heights[i][j]:
                        dfs(dx, dy, vis)
        
        pac, atl = set(), set()
        for i in range(m): dfs(0, i, pac)
        for j in range(n): dfs(j, 0, pac)
        for i in range(m): dfs(n-1, i, atl)
        for j in range(n): dfs(j, m-1, atl)

        return list(pac & atl)