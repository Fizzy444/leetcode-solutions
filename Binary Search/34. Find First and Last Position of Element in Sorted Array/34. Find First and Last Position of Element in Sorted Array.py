class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = nums.index(target) if target in nums else -1
        j = len(nums) - 1 - nums[::-1].index(target) if target in nums else -1
        if i and j == -1:
            j = i
        elif j and i == -1:
            i = j
        return [i, j]