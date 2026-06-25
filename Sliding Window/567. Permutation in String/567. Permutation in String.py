class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        d1 = {}
        d2 = {}
        k = len(s1)
        for i in range(k):
            d1[s1[i]] = d1.get(s1[i], 0) + 1
            d2[s2[i]] = d2.get(s2[i], 0) + 1
        
        if d1 == d2:
            return True
        i = 0
        for j in range(k, len(s2)):
            d2[s2[i]] -= 1
            if d2[s2[i]] == 0:
                d2.pop(s2[i])
            i += 1
            d2[s2[j]] = d2.get(s2[j], 0) + 1
            if d1 == d2:
                return True
        return False