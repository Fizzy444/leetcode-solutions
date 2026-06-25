class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        miss = 0
        dup = 0
        for i in nums:
            if i in s:
                dup = i
            s.add(i)
        for i in range(1,len(nums)+1):
            if i not in s:
                miss = i
                break
        return [dup,miss]