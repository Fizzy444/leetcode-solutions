class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        l = len(nums)
        med = l//2
        c = 0
        for i in range(med):
            c += nums[med] - nums[i]
        for i in range(med + 1, l):
            c += nums[i] - nums[med]
        return c