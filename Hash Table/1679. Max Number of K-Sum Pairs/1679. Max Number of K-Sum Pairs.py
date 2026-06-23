class Solution(object):
    def maxOperations(self, nums, k):
        d = {}
        count = 0
        for num in nums:
            target = k - num
            if target in d and d[target] > 0:
                count += 1
                d[target] -= 1
            else:
                if num not in d:
                    d[num] = 0
                d[num] += 1
        return count