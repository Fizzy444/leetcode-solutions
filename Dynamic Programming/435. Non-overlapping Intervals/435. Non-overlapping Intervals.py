class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rm = 0
        last = intervals[0][1]
        for s, e in intervals[1:]:
            if s < last:
                rm += 1
                last = min(last, e) 
            else:
                last = e
        return rm