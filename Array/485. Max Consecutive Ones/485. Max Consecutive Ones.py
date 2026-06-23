class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        c = 0
        l = len(nums)
        for i in range(l):
            if nums[i] == 1:
                c += 1
                m = max(m,c)
            else:
                c = 0
        return m