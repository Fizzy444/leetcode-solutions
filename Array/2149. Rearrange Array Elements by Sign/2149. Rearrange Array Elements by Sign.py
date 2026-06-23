class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1 = []
        l2 = []
        r = []
        for i in nums:
            if i < 0:
                l1.append(i)
            else:
                l2.append(i)
        for i in range(len(l1)):
            r.append(l2[i])
            r.append(l1[i])
        return r