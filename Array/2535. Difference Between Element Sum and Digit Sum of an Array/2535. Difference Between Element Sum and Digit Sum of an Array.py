class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = 0
        s2 = 0
        for i in nums:
            s1 += i
            while i:
                s2 += i%10
                i //= 10
        return abs(s1-s2)