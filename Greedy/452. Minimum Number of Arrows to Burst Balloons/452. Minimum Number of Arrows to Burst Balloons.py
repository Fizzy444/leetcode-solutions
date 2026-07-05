class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        arrow = 1
        pos = points[0][1]
        for s, e in points[1:]:
            if s > pos:
                arrow += 1
                pos = e
        return arrow