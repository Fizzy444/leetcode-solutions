class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1 = {}
        d2 = {}
        res = []
        k = len(p)
        if k > len(s):
            return []
        for i in range(k):
            d1[p[i]] = d1.get(p[i], 0) + 1
            d2[s[i]] = d2.get(s[i], 0) + 1
        
        if d1 == d2:
            res.append(0)
        
        i = 0

        for j in range(k, len(s)):
            d2[s[i]] -= 1
            if d2[s[i]] == 0:
                d2.pop(s[i])
            
            i += 1

            d2[s[j]] = d2.get(s[j], 0) + 1
            if d1 == d2:
                res.append(i)
        return res