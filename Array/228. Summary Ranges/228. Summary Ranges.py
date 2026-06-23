class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        r = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1
            end = nums[i]
            if start == end:
                r.append(str(start))
            else:
                r.append(str(start) + "->" + str(end))
            i += 1
        return r