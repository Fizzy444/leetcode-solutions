class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        r = 0
        for i in nums:
            r += m-i
        return r