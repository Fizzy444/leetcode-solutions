class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        m = 0
        print(d)
        for k,v in d.items():
            if v > len(nums)//2:
                m = k
                break
        return m