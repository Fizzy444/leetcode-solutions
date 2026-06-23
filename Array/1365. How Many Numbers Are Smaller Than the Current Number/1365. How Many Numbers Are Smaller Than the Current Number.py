class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        l = len(nums)
        for i in range(l):
            c = 0
            for j in range(l):
                if nums[i] > nums[j]:
                    c += 1
            r.append(c)
        return r