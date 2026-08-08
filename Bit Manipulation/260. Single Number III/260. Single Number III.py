class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        res = []
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for k, v in d.items():
            if v == 1:
                res.append(k)
        return res