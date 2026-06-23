class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = 0
        d = 0
        for i in nums:
            if i < 10:
                s += i
            else:
                d += i
        if s == d:
            return False
        return True