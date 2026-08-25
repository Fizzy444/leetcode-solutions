class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        t = k
        while True:
            if t not in nums:
                return t
            else:
                t += k      