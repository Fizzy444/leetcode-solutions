class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = nums[0]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum>max_num:
                max_num = sum
            
            if sum<0:
                sum=0
        return max_num