class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        curr = 0
        m = 0
        for i in range(len(nums)):
            curr += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            if i >= k:
                freq[nums[i-k]] -= 1
                curr -= nums[i-k]
                if freq[nums[i-k]] == 0:
                    del freq[nums[i-k]]
            if i >= k - 1 and len(freq) == k:
                m = max(m, curr)
        return m