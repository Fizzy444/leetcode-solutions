class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        res = []
        def dfs(node, path):
            path.append(node)
            if node == n:
                res.append(path.copy())
                path.pop()
                return
            for j in graph[node]:
                dfs(j, path)
            path.pop()
        dfs(0, [])
        return res