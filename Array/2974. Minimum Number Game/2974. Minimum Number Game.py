class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = sorted(nums)
        for i in range(0,len(res),2):
            res[i], res[i+1] = res[i+1], res[i]
        return res