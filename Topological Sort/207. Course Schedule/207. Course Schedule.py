class Solution:
    def canFinish(self, num: int, graph: list[list[int]]) -> bool:
        adj = [[] for _ in range(num)]

        for course, pre in graph:
            adj[pre].append(course)

        color = [0] * num

        def dfs(i):
            color[i] = 1

            for j in adj[i]:
                if color[j] == 1:
                    return False

                if color[j] == 0:
                    if not dfs(j):
                        return False

            color[i] = 2
            return True

        for i in range(num):
            if color[i] == 0:
                if not dfs(i):
                    return False

        return True