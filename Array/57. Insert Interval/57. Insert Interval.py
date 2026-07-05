class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])

        ans = [intervals[0]]

        for start, end in intervals[1:]:
            last = ans[-1][1]
            if start <= last:
                ans[-1][1] = max(last, end)
            else:
                ans.append([start, end])
        return ans