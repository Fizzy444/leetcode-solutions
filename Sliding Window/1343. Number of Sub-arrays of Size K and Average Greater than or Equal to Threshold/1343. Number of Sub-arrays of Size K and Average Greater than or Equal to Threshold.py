class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        s = 0
        c = 0
        for j in range(len(arr)):
            s += arr[j]
            if j >= k - 1:
                if s//k >= threshold:
                    c += 1
                s -= arr[i]
                i += 1
        return c