class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr = []
        l = len(intervals)
        i = 0
        while i < l:
            j = i + 1
            s = intervals[i][0]
            e = intervals[i][1]
            while j < l and intervals[j][0] <= e:
                e = max(e, intervals[j][1])
                j += 1
            i = j
            arr.append([s, e])
        return arr