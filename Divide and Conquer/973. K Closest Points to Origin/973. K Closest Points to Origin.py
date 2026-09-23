class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        p = {}

        for point in points:
            x = point[0]
            y = point[1]
            distance = x**2 + y**2

            p.setdefault(distance, []).append(point)

        arr = sorted(p.keys())

        ans = []

        for distance in arr:
            for point in p[distance]:
                if len(ans) == k:
                    return ans
                ans.append(point)

        return ans